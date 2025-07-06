from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from flights.filters import OrderFilter
from flights.models import Order
from flights.serializers.order import (
    OrderSerializer,
    OrderListSerializer,
    OrderDetailSerializer
)


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderFilter

    def get_serializer_class(self):
        if self.action == "list":
            return OrderListSerializer
        if self.action == "retrieve":
            return OrderDetailSerializer
        return OrderSerializer

    def get_queryset(self):
        return (
            Order.objects.filter(
                user=self.request.user
            ).prefetch_related(
                "tickets__flight__route__source",
                "tickets__flight__route__destination",
                "tickets__flight__airplane"
            ).select_related("user")
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
