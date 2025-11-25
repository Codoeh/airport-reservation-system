from datetime import datetime

import pytest
from rest_framework.test import APIClient

from tests.factories.flights_factories import (
    AirportFactory,
    AirplaneTypeFactory,
    AirplaneFactory,
    RouteFactory,
    FlightFactory, OrderFactory, TicketFactory
)
from tests.factories.user_factories import UserFactory


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user(db):
    user = UserFactory(username="tester")
    user.set_password("1qazCDE#")
    user.save()
    return user


@pytest.fixture
def authenticated_client(api_client, user):
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture
def source_airport():
    return AirportFactory(
        name="JFK",
        closest_big_city="New York"
    )


@pytest.fixture
def destination_airport():
    return AirportFactory(
        name="LAX",
        closest_big_city="Los Angeles"
    )


@pytest.fixture
def airplane_type():
    return AirplaneTypeFactory(name="Boeing 737")


@pytest.fixture
def airplane(airplane_type):
    return AirplaneFactory(
        airplane_type=airplane_type,
        name="PlaneA"
    )


@pytest.fixture
def route(source_airport, destination_airport):
    return RouteFactory(
        source=source_airport,
        destination=destination_airport,
        distance=4500
    )


@pytest.fixture
def flight(airplane, route):
    return FlightFactory(
        airplane=airplane,
        route=route,
        departure_time=datetime(2030, 1, 1, 10, 0),
        arrival_time=datetime(2030, 1, 1, 14, 0)
    )


@pytest.fixture
def invalid_ticket_data(flight):
    return {"seat": 20, "row": 20, "flight": flight.id}


@pytest.fixture
def order_with_tickets(user, flight):
    order = OrderFactory(user=user)
    TicketFactory.create_batch(
        8,
        order=order,
        flight=flight
    )
    return order
