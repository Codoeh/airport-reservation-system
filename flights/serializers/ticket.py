from rest_framework import serializers

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

    def get_order(self, obj):
        from .order import OrderSerializer
        return OrderSerializer(obj.order).data
