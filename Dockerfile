# syntax=docker/dockerfile:1
# Based on https://docs.astral.sh/uv/guides/integration/docker/
# Keep PYTHON_VERSION identical in both stages: the venv links to that interpreter.
ARG PYTHON_VERSION=3.14
ARG UV_VERSION=0.13.9

FROM ghcr.io/astral-sh/uv:${UV_VERSION}-python${PYTHON_VERSION}-trixie-slim AS builder

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_NO_DEV=1 \
    UV_PYTHON_DOWNLOADS=0

WORKDIR /app

# Dependencies only: this layer is rebuilt only when uv.lock or pyproject.toml change.
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-editable

# Project itself, installed non-editable so the runtime only needs the venv.
COPY . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-editable


FROM python:${PYTHON_VERSION}-slim-trixie AS runtime

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/app/.venv/bin:$PATH"

RUN useradd --system --uid 10001 --no-create-home --shell /usr/sbin/nologin appuser

COPY --from=builder /app/.venv /app/.venv

USER appuser
WORKDIR /app

# For a long-running service, uncomment and point it at a real health endpoint.
# Docker then marks the container unhealthy when the app stops responding.
# HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
#     CMD ["python", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:8000/health', timeout=3)"]

ENTRYPOINT ["app"]
