import django_filters
from flights.models.flight import Flight
from flights.models.crew import Crew
from flights.models.route import Route
from flights.models.airplane import Airplane
from flights.models.airplane_type import AirplaneType
from flights.models.ticket import Ticket
from flights.models.order import Order
from flights.models.airport import Airport


class CrewFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr="icontains")
    last_name = django_filters.CharFilter(lookup_expr="icontains")
    flights = django_filters.NumberFilter(field_name="flights__id")

    class Meta:
        model = Crew
        fields = ["first_name", "last_name", "flights"]


class RouteFilter(django_filters.FilterSet):
    source = django_filters.CharFilter(
        field_name="source__name", lookup_expr="icontains"
    )
    destination = django_filters.CharFilter(
        field_name="destination__name", lookup_expr="icontains"
    )
    distance = django_filters.NumberFilter()
    distance__gte = django_filters.NumberFilter(
        field_name="distance", lookup_expr="gte"
    )
    distance__lte = django_filters.NumberFilter(
        field_name="distance", lookup_expr="lte"
    )

    class Meta:
        model = Route
        fields = [
            "source",
            "destination",
            "distance",
            "distance__gte",
            "distance__lte",
        ]


class AirplaneFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    airplane_type = django_filters.CharFilter(
        field_name="airplane_type__name",
        lookup_expr="icontains"
    )

    class Meta:
        model = Airplane
        fields = ["name", "airplane_type"]


class AirplaneTypeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = AirplaneType
        fields = [
            "name",
        ]


class AirportFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    closest_big_city = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Airport
        fields = ["name", "closest_big_city"]


class TicketFilter(django_filters.FilterSet):
    row = django_filters.NumberFilter()
    seat = django_filters.NumberFilter()
    flight = django_filters.NumberFilter(field_name="flight")
    order = django_filters.NumberFilter(field_name="order")
    order_date = django_filters.DateFromToRangeFilter(
        field_name="order__created_at"
    )

    class Meta:
        model = Ticket
        fields = ["row", "seat", "flight", "order", "order_date"]


class OrderFilter(django_filters.FilterSet):
    created_at = django_filters.DateFromToRangeFilter(field_name="created_at")

    class Meta:
        model = Order
        fields = ["created_at"]


class FlightFilter(django_filters.FilterSet):
    departure_time = django_filters.DateTimeFromToRangeFilter(
        field_name="departure_time"
    )
    arrival_time = django_filters.DateTimeFromToRangeFilter(
        field_name="arrival_time"
    )
    route = django_filters.CharFilter(field_name="route")
    airplane = django_filters.CharFilter(field_name="airplane")
    crew = django_filters.NumberFilter(field_name="crew__id")

    class Meta:
        model = Flight
        fields = [
            "departure_time",
            "arrival_time",
            "route",
            "airplane",
            "crew"
        ]
