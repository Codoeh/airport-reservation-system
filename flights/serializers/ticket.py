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
        read_only_fields = ("id",)
