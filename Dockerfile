FROM python:3.13-slim

RUN pip install uv

WORKDIR /app

COPY pyproject.toml uv.lock .

RUN uv sync --locked

ENV PATH="/app/.venv/bin:$PATH"

COPY . .
