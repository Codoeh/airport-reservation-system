from rest_framework import viewsets

from flights.serializers.route import RouteSerializer
from flights.models.route import Route


class RouteViewSet(viewsets.ModelViewSet):
    serializer_class = RouteSerializer
    queryset = Route.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == "list":
            queryset = queryset.select_related("source", "destination")
        return queryset
