from rest_framework import serializers

from ..models.airplane_type import AirplaneType


class AirplaneTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirplaneType
        fields = (
            "id",
            "name",
        )
        read_only_fields = ("id",)
