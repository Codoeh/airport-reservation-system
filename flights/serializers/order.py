from rest_framework import serializers

from ..models.order import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "id",
            "created_at",
            "user",
        )
        read_only_fields = ("id",)
