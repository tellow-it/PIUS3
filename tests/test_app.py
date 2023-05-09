from typing import Generator

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.base import Base
from db.session import get_db
from core.config import settings
from main import app

SQLALCHEMY_DATABASE_URL = settings.DATABASE_TEST_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db() -> Generator:  # new
    try:
        db = TestSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_get_important():
    response = client.get("/v1/important/")
    assert response.status_code == 200


def test_get_important_by_id():
    response = client.get("/v1/important/500")
    assert response.status_code == 200
    assert response.json()['data'] is None


def test_create_exist_important():
    response = client.post(
        "/v1/important/create/",
        json={"level": "low"},
    )
    assert response.status_code == 500


def test_create_important():
    response = client.post(
        "/v1/important/create/",
        json={"level": "medium"},
    )
    assert response.status_code == 201


def test_update_important():
    response = client.put(
        "/v1/important/update/",
        json={"id": 1, "level": "medium-2"},
    )
    assert response.status_code == 200


def test_get_categories():
    response = client.get("/v1/categories/")
    assert response.status_code == 200


def test_get_category_by_id():
    response = client.get("/v1/categories/500")
    assert response.status_code == 200
    assert response.json()['data'] is None


def test_create_category():
    response = client.post(
        "/v1/categories/create/",
        json={"name": "routine"},
    )
    assert response.status_code == 201


def test_create_exist_category():
    response = client.post(
        "/v1/categories/create/",
        json={"name": "routine"},
    )
    assert response.status_code == 500


def test_update_category():
    response = client.put("/v1/categories/update/",
                          json={
                              "name": "routine-1",
                              "id": 1
                          }
                          )
    assert response.status_code == 200


def test_get_tasks():
    response = client.get("/v1/tasks/")
    assert response.status_code == 200


def test_get_task_by_id():
    response = client.get("/v1/tasks/500")
    assert response.status_code == 200
    assert response.json()['data'] is None


def test_create_task():
    response = client.post(
        "/v1/tasks/create/",
        json={"name": "lab",
              "description": "lab lab",
              "date_create": "2023-05-09T12:41:26.484Z",
              "status": False,
              "deadline": "2023-05-09T12:41:26.484Z",
              "category_id": 1,
              "important_id": 1},
    )
    assert response.status_code == 201


def test_create_error_task():
    response = client.post(
        "/v1/tasks/create/",
        json={"name": "lab",
              "description": "lab lab",
              "date_create": "2023-05-09T12:41:26.484Z",
              "status": False,
              "deadline": "2023-05-09T12:41:26.484Z",
              "category_id": 1,
              "important_id": 33},
    )
    assert response.status_code == 500


def test_update_task():
    response = client.put(
        "/v1/tasks/update/",
        json={"name": "lab33",
              "description": "lab lab",
              "date_create": "2023-05-09T12:41:26.484Z",
              "status": False,
              "deadline": "2023-05-09T12:41:26.484Z",
              "category_id": 1,
              "important_id": 1,
              "id": 1},
    )
    assert response.status_code == 200


def test_update_status_task():
    response = client.patch(
        "/v1/tasks/update_status/",
        json={"status": True,
              "id": 1},
    )
    assert response.status_code == 200


# delete tests

def test_delete_important():
    response = client.delete("/v1/important/delete/1")
    assert response.status_code == 200


def test_delete_category():
    response = client.delete("/v1/categories/delete/1")
    assert response.status_code == 200


def test_delete_task():
    response = client.delete("/v1/tasks/delete/2")
    assert response.status_code == 200
