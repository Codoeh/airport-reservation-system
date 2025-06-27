from rest_framework import viewsets
from flights.models.crew import Crew
from flights.serializers.crew import CrewSerializer


class CrewViewSet(viewsets.ModelViewSet):
    serializer_class = CrewSerializer
    queryset = Crew.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == "list":
            queryset = queryset.prefetch_related("flights")
        return queryset
