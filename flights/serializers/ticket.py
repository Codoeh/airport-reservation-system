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

    def validate(self, data):
        flight = data["flight"]
        row = data["row"]
        seat = data["seat"]
        airplane = flight.airplane

        if row > airplane.rows or seat > airplane.seats_in_row:
            raise serializers.ValidationError("Seat or row is out of range.")
        return data


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


class TicketInOrdersSerializer(serializers.ModelSerializer):
    seat_number = serializers.SerializerMethodField()
    flight = FlightInOrdersSerializer(
        read_only=True,
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

    def get_seat_number(self, obj):
        return ((obj.row - 1) * 10) + obj.seat


class TicketInOrderListSerializer(TicketSerializer):
    class Meta:
        model = Ticket
        fields = [
            "id",
            "row",
            "seat",
            "flight",
            "seat_number",
        ]
