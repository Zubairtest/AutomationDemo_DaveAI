import requests

BASE_URL = "https://reqres.in/api"
HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

def test_successful_get_user():
    """Validate a successful response (status code 200) for user ID 2"""
    response = requests.get(f"{BASE_URL}/users/2", headers=HEADERS)
    assert response.status_code == 200

def test_response_content_user_data():
    """Validate that response contains expected user data for user ID 2"""
    response = requests.get(f"{BASE_URL}/users/2", headers=HEADERS)
    data = response.json()
    assert "data" in data
    assert data["data"]["id"] == 2
    assert data["data"]["email"] == "janet.weaver@reqres.in"
    
def test_login_missing_password():
    """Validate error when required field is missing (400)"""
    payload = {"email": "peter@klaven"}  # Missing password
    response = requests.post(f"{BASE_URL}/login", json=payload, headers=HEADERS)
    assert response.status_code == 400
    data = response.json()
    assert "error" in data
    assert data["error"] == "Missing password"

def test_user_not_found():
    """Validate error handling for non-existing user"""
    response = requests.get(f"{BASE_URL}/users/9999", headers=HEADERS)
    assert response.status_code == 404
    assert response.text == "{}"

def test_create_user_missing_field():
    """Simulate error with incomplete payload"""
    payload = {}  # missing fields
    response = requests.post(f"{BASE_URL}/users", json=payload, headers=HEADERS)
    assert response.status_code == 201  
    data = response.json()
    assert "id" in data
