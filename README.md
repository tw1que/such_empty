# Inventory App

This repository contains a minimal inventory application with a FastAPI backend and a Next.js frontend.

## Quickstart

```bash
cp .env.example .env
make up
make backend-migrate
```

Open http://localhost:3000 to view the app.

See `backend/README.md` and `frontend/README.md` for more details.

## CI
- Backend en frontend draaien als losse jobs.
- Backend gebruikt een Postgres service op CI via `DATABASE_URL`.
- Checks draaien op `push` en `pull_request`; je ziet daardoor twee entries per job.
