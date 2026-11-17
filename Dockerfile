FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml kaedemeta_mcp.py README.md ./
RUN pip install --no-cache-dir .
CMD ["kaedemeta-mcp"]
