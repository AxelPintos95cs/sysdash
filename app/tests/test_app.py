from app import app

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "ok"}

def test_create_user():
    client = app.test_client()
    response = client.post("/users", json={"name": "Axel", "email": "axel@example.com"})
    assert response.status_code == 201
    assert response.json["name"] == "Axel"
    assert response.json["email"] == "axel@example.com"

def test_get_users():
    client = app.test_client()
    # Primero crear usuario para asegurar que no esté vacío
    client.post("/users", json={"name": "Test", "email": "test@example.com"})
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json, list)
