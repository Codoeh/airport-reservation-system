from django.db.models import Prefetch
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from flights.filters import CrewFilter
from flights.models import Flight
from flights.models.crew import Crew
from flights.serializers.crew import (
    CrewSerializer,
    CrewListSerializer,
    CrewDetailSerializer,
)


class CrewViewSet(viewsets.ModelViewSet):
    queryset = Crew.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = CrewFilter

    def get_serializer_class(self):
        if self.action == "list":
            return CrewListSerializer
        if self.action == "retrieve":
            return CrewDetailSerializer
        return CrewSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action in ["list", "retrieve"]:
            queryset = queryset.prefetch_related(
                Prefetch(
                    "flights",
                    queryset=Flight.objects.select_related(
                        "route__source",
                        "route__destination",
                        "airplane__airplane_type",
                    ),
                )
            )
        return queryset
