#! /usr/bin/env bash

set -e
set -x

cd apps/agent
FASTAPI_ENV=development uv run python -c "import app.main; import json; print(json.dumps(app.main.app.openapi()))" > ../openapi.json
cd ..
mv openapi.json web/
bun run --filter web generate-client
bun run lint
