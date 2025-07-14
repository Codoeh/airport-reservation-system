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
