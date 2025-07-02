from rest_framework import serializers

from ..models import Order
from ..models.ticket import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = (
            "id",
            "row",
            "seat",
            "flight",
            "order",
        )
        read_only_fields = ("id", "order")

class TicketDetailSerializer(serializers.ModelSerializer):
    flight = serializers.StringRelatedField()
    order = serializers.StringRelatedField()

    class Meta:
        model = Ticket
        fields = (
            "id",
            "row",
            "seat",
            "flight",
            "order",
        )
        read_only_fields = ("id",)


class TicketListSerializer(TicketSerializer):
    order_date = serializers.DateTimeField(source="order.created_at", read_only=True)

    class Meta:
        model = Ticket
        fields = (
            "id",
            "row",
            "seat",
            "flight",
            "order",
            "order_date",
        )
        read_only_fields = ("id", "order")

    def get_order(self, obj):
        from .order import OrderSerializer
        return OrderSerializer(obj.order).data
