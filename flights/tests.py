import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from flights.models import AirplaneType, Airplane
from flights.models import Airport, Route, Flight, Order
from flights.serializers.ticket import TicketSerializer


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user(db):
    return User.objects.create_user(username="testuser", password="pass1234")


@pytest.fixture
def authenticated_client(api_client, user):
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture
def airport1():
    return Airport.objects.create(name="JFK", closest_big_city="New York")


@pytest.fixture
def airport2():
    return Airport.objects.create(name="LAX", closest_big_city="Los Angeles")


@pytest.fixture
def airplane_type():
    return AirplaneType.objects.create(name="Boeing 737")


@pytest.fixture
def airplane(airplane_type):
    return Airplane.objects.create(
        name="PlaneA",
        rows=5,
        seats_in_row=4,
        airplane_type=airplane_type
    )


@pytest.fixture
def route(airport1, airport2):
    return Route.objects.create(
        source=airport1,
        destination=airport2,
        distance=4500
    )


@pytest.fixture
def flight(airplane, route):
    from datetime import datetime
    return Flight.objects.create(
        airplane=airplane,
        route=route,
        departure_time=datetime(2030, 1, 1, 10, 0),
        arrival_time=datetime(2030, 1, 1, 14, 0)
    )


@pytest.mark.django_db
def test_airplane_total_seats():
    airplane_type = AirplaneType.objects.create(name="Test Type")
    airplane = Airplane.objects.create(
        name="X",
        rows=6,
        seats_in_row=4,
        airplane_type=airplane_type
    )
    assert airplane.total_seats == 24


@pytest.mark.django_db
def test_seat_number_calculation(flight, user):
    serializer = TicketSerializer(
        data={
            "row": 2,
            "seat": 3,
            "flight": flight.id
        }
    )
    assert serializer.is_valid()
    order = Order.objects.create(user=user)
    serializer.save(order=order)
    assert serializer.data["seat_number"] == 13


@pytest.mark.django_db
def test_airplane_list(authenticated_client, airplane):
    response = authenticated_client.get("/api/airplanes/")
    assert response.status_code == 200
    assert response.data["results"][0]["name"] == airplane.name


@pytest.mark.django_db
def test_flight_tickets_available(authenticated_client, flight):
    response = authenticated_client.get("/api/flights/")
    assert response.status_code == 200
    assert (response.data["results"][0]["tickets_available"] ==
            flight.airplane.total_seats)


@pytest.mark.django_db
def test_create_order(authenticated_client, flight):
    data = {
        "tickets": [{"flight": flight.id, "row": 1, "seat": 1}]
    }
    response = authenticated_client.post("/api/orders/", data, format="json")
    assert response.status_code == 201
    assert response.data["tickets"][0]["seat"] == 1


@pytest.mark.django_db
def test_invalid_ticket_seat(flight, user):
    serializer = TicketSerializer(data={
        "seat": 20,
        "row": 20,
        "flight": flight.id
    })
    assert not serializer.is_valid()
    errors = serializer.errors.get("non_field_errors", [])
    assert any("Seat or row is out of range."
               in str(error) for error in errors)


@pytest.mark.django_db
def test_many_tickets_order(authenticated_client, flight):
    data = {
        "tickets": [
            {
                "row": 1,
                "seat": 1,
                "flight": flight.id
            },
            {
                "row": 1,
                "seat": 2,
                "flight": flight.id
            },
        ]
    }
    response = authenticated_client.post("/api/orders/", data, format="json")
    assert response.status_code == 201
    assert len(response.data["tickets"]) == 2


@pytest.mark.django_db
def test_ticket_seat_collision(authenticated_client, flight):
    data = {
        "tickets": [{"flight": flight.id, "row": 1, "seat": 1}]
    }
    response = authenticated_client.post("/api/orders/", data, format="json")
    assert response.status_code == 201
    assert response.data["tickets"][0]["seat"] == 1
    response = authenticated_client.post("/api/orders/", data, format="json")
    assert response.status_code == 400


@pytest.mark.django_db
def test_order_delete(authenticated_client, flight):
    data = {
        "tickets": [{"flight": flight.id, "row": 1, "seat": 1}]
    }
    response = authenticated_client.post("/api/orders/", data, format="json")
    assert response.status_code == 201
    response = authenticated_client.delete("/api/orders/1/")
    assert response.status_code == 204
    response = authenticated_client.get("/api/orders/1/")
    assert response.status_code == 404


@pytest.mark.django_db
def test_pagination(authenticated_client, airplane_type):
    for i in range(10):
        Airplane.objects.create(
            name=f"plane_{i}",
            rows=5,
            seats_in_row=5,
            airplane_type=airplane_type
        )
    response = authenticated_client.get("/api/airplanes/")
    assert response.status_code == 200
    data = response.json()
    assert "results" in data
    assert len(data["results"]) == 5
