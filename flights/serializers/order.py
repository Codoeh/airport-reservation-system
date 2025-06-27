from rest_framework import serializers

from ..models.order import Order, User


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field="username",
    )
    class Meta:
        model = Order
        fields = (
            "id",
            "created_at",
            "user",
        )
        read_only_fields = ("id",)
