from django.db import transaction
from rest_framework import serializers

from .ticket import TicketSerializer, TicketInOrdersSerializer
from ..models import Ticket
from ..models.order import Order


class OrderSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True, read_only=False, allow_empty=False)
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username",
    )

    class Meta:
        model = Order
        fields = (
            "id",
            "created_at",
            "user",
            "tickets",
        )
        read_only_fields = ("id",)

    def create(self, validated_data):
        request = self.context.get("request")
        tickets_data = validated_data.pop("tickets")
        user = request.user
        validated_data.pop("user", None)
        with transaction.atomic():
            order = Order.objects.create(user=user, **validated_data)
            for ticket_data in tickets_data:
                ticket_data.pop("order", None)
                Ticket.objects.create(order=order, **ticket_data)
            return order


class OrderListSerializer(OrderSerializer):
    tickets = TicketInOrdersSerializer(many=True, read_only=True)
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username",
    )

    class Meta:
        model = Order
        fields = (
            "id",
            "created_at",
            "user",
            "tickets",
        )
        read_only_fields = ("id",)
