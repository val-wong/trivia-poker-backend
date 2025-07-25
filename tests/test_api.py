from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_random_trivia():
    response = client.get("/trivia/random")
    assert response.status_code == 200
    data = response.json()
    assert "question" in data
    assert "options" in data
    assert "correct_answer" in data
