from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from flights.filters import TicketFilter
from flights.models import Ticket
from flights.serializers.ticket import TicketSerializer, TicketDetailSerializer, TicketListSerializer


class TicketViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ticket.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = TicketFilter

    def get_serializer_class(self):
        if self.action == "retrieve":
            return TicketDetailSerializer
        if self.action == "list":
            return TicketListSerializer
        return TicketSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == "list":
            queryset = queryset.select_related("flight", "order")
        return queryset
