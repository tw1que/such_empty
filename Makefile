up:
docker compose up --build -d
down:
docker compose down -v
logs:
docker compose logs -f --tail=200
backend-migrate:
docker compose exec backend alembic upgrade head
backend-revision:
docker compose exec -e MSG="$(msg)" backend alembic revision --autogenerate -m "$$MSG"
fmt:
docker compose exec backend bash -lc "black app && isort app"
lint:
docker compose exec backend bash -lc "flake8 app && mypy app"
test:
docker compose exec backend pytest -q
