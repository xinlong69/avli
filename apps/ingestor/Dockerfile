# ==========================================
# STAGE 1: Build environment (Debian Slim)
# ==========================================
FROM python:3.13-slim AS builder

ENV PYTHONUNBUFFERED=1
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

# Install uv safely from its binary source
COPY --from=ghcr.io/astral-sh/uv:0.12.5 /uv /uvx /bin/

WORKDIR /app/

# Install workspace/library dependencies using your optimized cache mounts
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-workspace --no-editable --package avli-ingestor

# Copy application layers explicitly
COPY ./apps/ingestor/scripts /app/ingestor/scripts
COPY ./apps/ingestor/pyproject.toml /app/ingestor/
COPY ./apps/ingestor/app /app/ingestor/app

# Sync project with --no-editable to guarantee self-contained source binaries
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-editable --package avli-ingestor


# ==========================================
# STAGE 2: Secure Production Runtime (Distroless)
# ==========================================
FROM gcr.io/distroless/python3-debian13:nonroot

ENV PYTHONUNBUFFERED=1

# Distroless runs as 'nonroot' by default, set workdir inside home/app space
WORKDIR /home/nonroot/app

# Copy the complete self-contained virtual environment and apps from builder
COPY --from=builder /app/.venv /home/nonroot/app/.venv
COPY --from=builder /app/ingestor /home/nonroot/app/ingestor

# Set internal execution paths directly to the virtual environment
ENV PATH="/home/nonroot/app/.venv/bin:$PATH"
ENV PYTHONPATH="/home/nonroot/app/ingestor"

WORKDIR /home/nonroot/app/ingestor/

# Run via absolute paths since shell evaluation is completely disabled
ENTRYPOINT ["/home/nonroot/app/.venv/bin/fastapi"]
CMD ["run", "--workers", "4"]
