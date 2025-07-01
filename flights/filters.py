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


class RouteFilter(django_filters.FilterSet):
    source = django_filters.CharFilter(field_name="source__name", lookup_expr="icontains")
    destination = django_filters.CharFilter(field_name="destination__name", lookup_expr="icontains")
    distance = django_filters.NumberFilter()
    distance__gte = django_filters.NumberFilter(field_name="distance", lookup_expr="gte")
    distance__lte = django_filters.NumberFilter(field_name="distance", lookup_expr="lte")

    class Meta:
        model = Route
        fields = ["source", "destination", "distance", "distance__gte", "distance__lte"]


class AirplaneFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    airplane_type = django_filters.CharFilter(field_name="airplane_type__name", lookup_expr="icontains")

    class Meta:
        model = Airplane
        fields = ["name", "airplane_type"]


class AirplaneTypeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = AirplaneType
        fields = ["name",]

