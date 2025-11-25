from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from flights.filters import AirportFilter
from flights.serializers.airport import AirportSerializer
from flights.models.airport import Airport


class AirportViewSet(viewsets.ModelViewSet):
    serializer_class = AirportSerializer
    queryset = Airport.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = AirportFilter
