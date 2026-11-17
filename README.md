# KaedeMeta MCP Server

**High-concurrency lossless media & structured metadata extraction MCP Server for AI Agents.**

Give Claude Desktop, Cursor, Windsurf, or any MCP-compatible agent the ability to resolve original uncompressed image URLs, highest-bitrate MP4 streams, multi-page manga sets, and Ugoira archives from **X (Twitter)**, **Pixiv**, and **Danbooru** — with zero local cookie maintenance.

- **Web Workbench & Instant API Keys:** [https://kaedemeta.com](https://kaedemeta.com)
- **Free Trial:** Claim **10 free credits** instantly on the workbench (no credit card required).

---

## Key Capabilities

- **Lossless Original Resolution:** Automatically upgrades media URLs to `:orig` / uncompressed master files and selects maximum-bitrate video variants.
- **Batch Creator & Tag Feeds:** Extract up to 24 posts per call from `@username` timelines, Pixiv creator portfolios, or Danbooru tag queries.
- **Zero-State Execution:** No media binaries or user session credentials are ever stored on our servers.
- **Success-Only Metering:** 0 credits deducted on upstream 4xx/5xx errors or empty feeds.

---

## Quick Setup

### Option A: Native Streamable HTTP / JSON-RPC (Recommended)

For clients supporting remote HTTP MCP endpoints (Cursor, Claude Desktop, OpenClaw, custom agents):

```json
{
  "mcpServers": {
    "kaedemeta": {
      "url": "https://api.kaedemeta.com/mcp?api_key=YOUR_KAEDEMETA_API_KEY"
    }
  }
}
```

### Option B: Local `uvx` Stdio Bridge

If your MCP host requires a local `stdio` command, run the zero-config Python bridge:

```json
  "mcpServers": {
    "kaedemeta": {
      "command": "uvx",
      "args": ["kaedemeta-mcp"],
      "env": {
        "KAEDEMETA_API_KEY": "YOUR_KAEDEMETA_API_KEY"
      }
    }
  }

```
---

## Exposed MCP Tools

| Tool Name | Description |
| :--- | :--- |
| `extract_post_metadata` | Extract structured metadata and original high-resolution media URLs from a single X, Pixiv, or Danbooru post URL/ID. |
| `extract_creator_feed` | Batch extract original media URLs and metadata from a creator profile (`@username`, `users/ID`) or Danbooru tag query. |

---

## Example Prompts for Your AI Agent

- *"Fetch the latest 24 original artworks from `https://www.pixiv.net/users/12345678` and summarize the tags and publishing dates."*
- *"Extract the uncompressed original images from `https://x.com/NASA`."*
- *"Query Danbooru for `scenery landscape` and give me the direct high-res file URLs."*

---

## License

MIT License. Official MCP Server implementation for the KaedeMeta Core API ([kaedemeta.com](https://kaedemeta.com)).
