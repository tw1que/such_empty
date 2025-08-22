from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.api.v1 import deps
from app.main import app
from app.models import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[deps.get_db] = override_get_db

client = TestClient(app)


def test_crud_locations():
    r = client.post("/api/v1/locations/", json={"code": "l1", "name": "Loc"})
    assert r.status_code == 200
    loc_id = r.json()["id"]

    r = client.get("/api/v1/locations/")
    assert r.status_code == 200
    assert len(r.json()) == 1

    r = client.put(
        f"/api/v1/locations/{loc_id}", json={"code": "l1", "name": "Loc2"}
    )
    assert r.status_code == 200
    assert r.json()["name"] == "Loc2"

    r = client.delete(f"/api/v1/locations/{loc_id}")
    assert r.status_code == 200
