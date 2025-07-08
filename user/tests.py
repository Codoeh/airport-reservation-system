import pytest
from django.contrib.auth.models import User

from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


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
def test_login(api_client):
    username = "tester"
    password = "1qazCDE#"
    data = {
        "username": "tester",
        "password": "1qazCDE#"
    }
    User.objects.create_user(username=username, password=password)
    response = api_client.post("/api/token/", data, format="json")
    assert response.status_code == 200
    assert "token" in response.data
