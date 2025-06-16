FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN useradd -m appuser

COPY --chown=appuser:appuser . .

USER appuser

ENTRYPOINT ["uv", "run", "-m", "src.app"]
