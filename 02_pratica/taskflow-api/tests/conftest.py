import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from app.main import app, repository  # noqa: E402


@pytest.fixture(autouse=True)
def clear_repository() -> None:
    repository.clear()


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)
