from rest_framework import viewsets

from flights.models import Airplane
from flights.serializers.airplane import AirplaneSerializer


class AirplaneViewSet(viewsets.ModelViewSet):
    serializer_class = AirplaneSerializer
    queryset = Airplane.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        airplane_types = self.request.query_params.get("airplane_types")

        if airplane_types:
            airplane_types_ids = [int(str_id) for str_id in airplane_types.split(",")]
            queryset = queryset.filter(airplane_type__id__in=airplane_types_ids)

        if self.action == "list":
            queryset = queryset.select_related("airplane_type")
        return queryset
