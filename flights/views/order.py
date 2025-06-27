from rest_framework import viewsets

from flights.models import Order
from flights.serializers.order import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
