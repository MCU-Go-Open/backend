from fastapi.testclient import TestClient
from gopen_backend.server import app

client = TestClient(app)

def test_ping():
    response = client.get("/PING")
    assert response.status_code == 200
    assert response.json() == "PONG"