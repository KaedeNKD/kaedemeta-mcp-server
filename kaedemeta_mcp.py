import os
import sys
import json
import httpx

ENDPOINT = os.getenv("KAEDEMETA_API_URL", "https://api.kaedemeta.com/mcp")
API_KEY = os.getenv("KAEDEMETA_API_KEY", "").strip()


def main() -> None:
    if not API_KEY:
        sys.stderr.write(
            "[kaedemeta-mcp] Missing KAEDEMETA_API_KEY environment variable. "
            "Claim 10 free trial credits at https://kaedemeta.com\n"
        )

    headers = {
        "Content-Type": "application/json",
        "X-API-Key": API_KEY,
        "User-Agent": "KaedeMeta-MCP-Bridge/1.0.0",
    }

    with httpx.Client(timeout=30.0) as client:
        for line in sys.stdin:
            raw = line.strip()
            if not raw:
                continue
            try:
                msg = json.loads(raw)
            except json.JSONDecodeError:
                continue

            # JSON-RPC notifications (no id) do not expect a response
            if "id" not in msg:
                try:
                    client.post(ENDPOINT, headers=headers, json=msg)
                except Exception:
                    pass
                continue

            try:
                resp = client.post(ENDPOINT, headers=headers, json=msg)
                if resp.status_code == 200:
                    sys.stdout.write(resp.text.strip() + "\n")
                    sys.stdout.flush()
                else:
                    err_obj = {
                        "jsonrpc": "2.0",
                        "id": msg.get("id"),
                        "error": {
                            "code": -32000,
                            "message": f"Upstream gateway HTTP {resp.status_code}: {resp.text[:200]}",
                        },
                    }
                    sys.stdout.write(json.dumps(err_obj) + "\n")
                    sys.stdout.flush()
            except Exception as exc:
                err_obj = {
                    "jsonrpc": "2.0",
                    "id": msg.get("id"),
                    "error": {
                        "code": -32603,
                        "message": f"Bridge connection error: {type(exc).__name__}: {exc}",
                    },
                }
                sys.stdout.write(json.dumps(err_obj) + "\n")
                sys.stdout.flush()


if __name__ == "__main__":
    main()