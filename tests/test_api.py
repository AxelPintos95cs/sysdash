import requests

BASE_URL = "http://localhost:5000"

def test_health():
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200

def test_db_status():
    response = requests.get(f"{BASE_URL}/db-status")
    assert response.status_code == 200

def test_create_and_get_users():
    # Crear usuario
    user_data = {"name": "Axel", "email": "example@test.com"}
    post_resp = requests.post(f"{BASE_URL}/users", json=user_data)
    assert post_resp.status_code == 201

    # Ver usuarios
    get_resp = requests.get(f"{BASE_URL}/users")
    assert get_resp.status_code == 200
    assert any(u["email"] == "example@test.com" for u in get_resp.json())
