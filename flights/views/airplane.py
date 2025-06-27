from rest_framework import viewsets

from flights.models import Airplane
from flights.serializers.airplane import AirplaneSerializer


class AirplaneViewSet(viewsets.ModelViewSet):
    serializer_class = AirplaneSerializer
    queryset = Airplane.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == "list":
            queryset = queryset.select_related("airplane_type")
        return queryset
