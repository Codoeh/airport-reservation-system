from rest_framework import viewsets

from flights.models.crew import Crew
from flights.serializers.crew import CrewSerializer, CrewListSerializer, CrewDetailSerializer


class CrewViewSet(viewsets.ModelViewSet):
    queryset = Crew.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return CrewListSerializer
        if self.action == "retrieve":
            return CrewDetailSerializer
        return CrewSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == "list":
            queryset = queryset.prefetch_related("flights")
        if self.action == "retrieve":
            queryset = queryset.prefetch_related("flights")
        return queryset
