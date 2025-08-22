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
- Backend gebruikt Postgres service op CI. Stel lokaal `DATABASE_URL` in of gebruik docker-compose.
- Checks lopen op zowel `push` als `pull_request`; daarom zie je twee entries per job.

