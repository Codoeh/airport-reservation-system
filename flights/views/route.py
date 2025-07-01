from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from flights.filters import RouteFilter
from flights.serializers.route import RouteSerializer
from flights.models.route import Route


class RouteViewSet(viewsets.ModelViewSet):
    serializer_class = RouteSerializer
    queryset = Route.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = RouteFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == "list":
            queryset = queryset.select_related("source", "destination")
        return queryset
