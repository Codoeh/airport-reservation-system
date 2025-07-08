from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from flights.filters import AirplaneFilter
from flights.models import Airplane
from flights.serializers.airplane import AirplaneSerializer


class AirplaneViewSet(viewsets.ModelViewSet):
    serializer_class = AirplaneSerializer
    queryset = Airplane.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = AirplaneFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == "list":
            queryset = queryset.select_related("airplane_type")
        return queryset
