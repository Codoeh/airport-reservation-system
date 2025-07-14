import factory

from flights.models import (
Airport,
Airplane,
AirplaneType,
Route,
Flight,
Order
)


class AirportFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Airport

    name = factory.Sequence(lambda n: f"Airport{n}")
    closest_big_city = factory.Sequence(lambda n: f"City{n}")


class AirplaneTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AirplaneType

    name = factory.Sequence(lambda n: f"Type{n}")


class AirplaneFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Airplane

    name = factory.Sequence(lambda n: f"Plane{n}")
    rows = 5
    seats_in_row = 4
    airplane_type = factory.SubFactory(AirplaneTypeFactory)


class RouteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Route

    source = factory.SubFactory(AirportFactory)
    destination = factory.SubFactory(AirportFactory)
    distance = 4500


class FlightFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Flight

    airplane = factory.SubFactory(AirplaneFactory)
    route = factory.SubFactory(RouteFactory)
    departure_time = factory.Faker("date_time_this_decade")
    arrival_time = factory.Faker("date_time_this_decade")
