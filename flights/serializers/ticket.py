from rest_framework import serializers

from .flight import FlightInOrdersSerializer
from ..models.ticket import Ticket


class TicketSerializer(serializers.ModelSerializer):
    seat_number = serializers.SerializerMethodField()

    class Meta:
        model = Ticket
        fields = (
            "id",
            "row",
            "seat",
            "flight",
            "order",
            "seat_number",
        )
        read_only_fields = ("id", "order")

    def get_seat_number(self, obj):
        return ((obj.row - 1) * 10) + obj.seat


class TicketDetailSerializer(TicketSerializer):
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
            "seat_number",
        )
        read_only_fields = ("id",)


class TicketListSerializer(TicketSerializer):
    order_date = serializers.DateTimeField(
        source="order.created_at",
        read_only=True
    )

    class Meta:
        model = Ticket
        fields = (
            "id",
            "row",
            "seat",
            "flight",
            "order",
            "order_date",
            "seat_number",
        )
        read_only_fields = ("id", "order")

    def get_order(self, obj):
        from .order import OrderSerializer

        return OrderSerializer(obj.order).data


class TicketInOrdersSerializer(TicketListSerializer):
    flight = FlightInOrdersSerializer(
        many=False,
        read_only=True
    )

    class Meta:
        model = Ticket
        fields = (
            "id",
            "row",
            "seat",
            "seat_number",
            "flight",
        )
        read_only_fields = ("id",)
