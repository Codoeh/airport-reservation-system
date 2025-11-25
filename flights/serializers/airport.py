from rest_framework import serializers

from ..models.airport import Airport


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = (
            "id",
            "name",
            "closest_big_city",
        )
        read_only_fields = ("id",)
