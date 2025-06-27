from rest_framework import viewsets

from flights.models import Ticket
from flights.serializers.ticket import TicketSerializer, TicketDetailSerializer


class TicketViewSet(viewsets.ModelViewSet):
    # serializer_class = TicketSerializer
    queryset = Ticket.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return TicketDetailSerializer
        return TicketSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == "list":
            queryset = queryset.select_related("flight", "order")
        return queryset
