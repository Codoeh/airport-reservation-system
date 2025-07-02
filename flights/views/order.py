from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from flights.filters import OrderFilter
from flights.models import Order
from flights.serializers.order import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderFilter

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
