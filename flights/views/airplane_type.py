from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from flights.filters import AirplaneTypeFilter
from flights.models import AirplaneType
from flights.serializers.airplane_type import AirplaneTypeSerializer


class AirplaneTypeViewSet(viewsets.ModelViewSet):
    serializer_class =  AirplaneTypeSerializer
    queryset = AirplaneType.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = AirplaneTypeFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == "list":
            queryset = queryset.prefetch_related("airplanes")
        return queryset
