from rest_framework import viewsets

from flights.models import AirplaneType
from flights.serializers.airplane_type import AirplaneTypeSerializer

class AirplaneTypeViewSet(viewsets.ModelViewSet):
    serializer_class =  AirplaneTypeSerializer

    def get_queryset(self):
        queryset = AirplaneType.objects.all()
        if self.action == "list":
            queryset = queryset.prefetch_related("airplanes")
        return queryset
