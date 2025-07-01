import django_filters
from flights.models.flight import Flight
from flights.models.crew import Crew
from flights.models.route import Route
from flights.models.airplane import Airplane
from flights.models.airplane_type import AirplaneType
from flights.models.ticket import Ticket
from flights.models.order import Order


class CrewFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr="icontains")
    last_name = django_filters.CharFilter(lookup_expr="icontains")
    flights = django_filters.NumberFilter(field_name="flights__id")

    class Meta:
        model = Crew
        fields = ["first_name", "last_name", "flights"]