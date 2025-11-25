import pytest


@pytest.mark.django_db
def test_register(api_client):
    data = {
        "username": "tester",
        "email": "tester@example.com",
        "password1": "1qazCDE#",
        "password2": "1qazCDE#"
    }
    response = api_client.post("/api/auth/registration/", data, format="json")
    assert response.status_code == 201 or response.status_code == 200


@pytest.mark.django_db
def test_login(api_client, user):
    data = {
        "username": "tester",
        "password": "1qazCDE#"
    }
    response = api_client.post("/api/token/", data, format="json")
    assert response.status_code == 200
    assert "token" in response.data
