FROM python:3.13.5-slim-bullseye

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN useradd -m appuser && \
    mkdir -p /app && \
    chown -R appuser:appuser /app

USER appuser

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:0.7.13 /uv /uvx /bin/

COPY --chown=appuser:appuser . .

RUN uv sync

ENTRYPOINT ["uv", "run", "-m", "src.app"]