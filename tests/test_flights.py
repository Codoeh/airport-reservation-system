import pytest

from flights.serializers.ticket import TicketSerializer
from tests.factories.flights_factories import AirplaneFactory, OrderFactory


@pytest.mark.django_db
def test_airplane_total_seats(airplane):
    assert airplane.total_seats == 20


@pytest.mark.django_db
def test_seat_number_calculation(flight, user):
    data = {
        "row": 2,
        "seat": 3,
        "flight": flight.id
    }

    serializer = TicketSerializer(data=data)
    assert serializer.is_valid()
    order = OrderFactory(user=user)
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
def test_invalid_ticket_seat(invalid_ticket_data):
    serializer = TicketSerializer(data=invalid_ticket_data)
    assert not serializer.is_valid()
    errors = serializer.errors.get("non_field_errors", [])
    assert any("Seat or row is out of range."
               in str(error) for error in errors)


@pytest.mark.django_db
def test_many_tickets_order(order_with_tickets):
    assert order_with_tickets.tickets.count() == 8


@pytest.mark.django_db
def test_ticket_seat_collision(authenticated_client, flight):
    data = {
        "tickets": [{"flight": flight.id, "row": 1, "seat": 1}]
    }
    # First booking should succeed
    response = authenticated_client.post("/api/orders/", data, format="json")
    assert response.status_code == 201
    assert response.data["tickets"][0]["seat"] == 1
    # Second booking for same seat should fail
    response = authenticated_client.post("/api/orders/", data, format="json")
    assert response.status_code == 400


@pytest.mark.django_db
def test_order_delete(authenticated_client, flight):
    data = {
        "tickets": [{"flight": flight.id, "row": 1, "seat": 1}]
    }
    response = authenticated_client.post("/api/orders/", data, format="json")
    assert response.status_code == 201
    order_id = response.data["id"]

    # Delete
    response = authenticated_client.delete(f"/api/orders/{order_id}/")
    assert response.status_code == 204

    # Ensure it's gone
    response = authenticated_client.get(f"/api/orders/{order_id}/")
    assert response.status_code == 404


@pytest.mark.django_db
def test_pagination(authenticated_client, airplane_type):
    AirplaneFactory.create_batch(10, airplane_type=airplane_type)
    response = authenticated_client.get("/api/airplanes/")
    assert response.status_code == 200
    data = response.json()
    assert "results" in data
    assert len(data["results"]) == 5
