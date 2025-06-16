FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN pip install --no-cache-dir uv

RUN useradd -m appuser

COPY --chown=appuser:appuser . .

USER appuser

ENTRYPOINT ["uv", "run", "-m", "src.app"]
