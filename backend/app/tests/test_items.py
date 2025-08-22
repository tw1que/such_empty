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


def override_token():
    return "test"


app.dependency_overrides[deps.get_db] = override_get_db
app.dependency_overrides[deps.get_current_token] = override_token

client = TestClient(app)


def test_crud_items():
    r = client.post("/api/v1/items/", json={"sku": "s1", "name": "Item"})
    assert r.status_code == 200
    item_id = r.json()["id"]

    r = client.get("/api/v1/items/")
    assert r.status_code == 200
    assert len(r.json()) == 1

    r = client.put(
        f"/api/v1/items/{item_id}",
        json={"sku": "s1", "name": "Item2", "description": None, "min_qty": 0, "is_active": True},
    )
    assert r.status_code == 200

    r = client.delete(f"/api/v1/items/{item_id}")
    assert r.status_code == 200
