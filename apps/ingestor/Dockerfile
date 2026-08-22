# ==========================================
# Stage 1: Builder
# ==========================================
FROM ghcr.io/astral-sh/uv:0.12.5-python3.13-bookworm-slim AS builder

ENV PYTHONUNBUFFERED=1
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

WORKDIR /app/

# 1. Install external third-party dependencies (cached layer)
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-workspace --no-editable --package avli-ingestor

# 2. Copy workspace package matching the root workspace layout
COPY ./apps/ingestor/scripts /app/ingestor/scripts
COPY ./apps/ingestor/pyproject.toml /app/ingestor/
COPY ./apps/ingestor/app /app/ingestor/app

# 3. Sync and install the workspace project
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-editable --package avli-ingestor


# ==========================================
# Stage 2: Runtime (Minimal slim image)
# ==========================================
FROM python:3.13-slim-bookworm AS runner

ENV PYTHONUNBUFFERED=1
ENV PATH="/app/.venv/bin:$PATH"

# Create the non-root user 'user' and grant passwordless sudo
RUN apt-get update && apt-get install -y --no-install-recommends sudo \
    && rm -rf /var/lib/apt/lists/* \
    && useradd -m -s /bin/bash -u 1000 user \
    && echo "user ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/user \
    && chmod 0440 /etc/sudoers.d/user

WORKDIR /app

# Copy the pre-built virtual environment and application files from builder
COPY --from=builder /app/.venv /app/.venv
COPY ./apps/ingestor /app/apps/ingestor

WORKDIR /app/apps/ingestor

USER user

CMD ["fastapi", "run", "--port", "9000", "--workers", "4"]
