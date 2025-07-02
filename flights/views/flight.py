from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from flights.filters import FlightFilter
from flights.models import Flight
from flights.serializers.flight import FlightSerializer, FlightListSerializer


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = FlightFilter

    def get_serializer_class(self):
        if self.action == "list":
            return FlightListSerializer
        return FlightSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == "list":
            queryset = queryset.select_related("airplane", "route")
        return queryset
