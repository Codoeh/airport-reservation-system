from rest_framework import serializers

from .flight import FlightSerializer
from .order import OrderSerializer
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
        read_only_fields = ("id",)

class TicketDetailSerializer(serializers.ModelSerializer):
    flight = FlightSerializer(many=False, read_only=True)
    order = OrderSerializer(many=False, read_only=True)

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
