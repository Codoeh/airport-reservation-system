from rest_framework import serializers

from flights.models.airport import Airport
from ..models.route import Route


class RouteSerializer(serializers.ModelSerializer):
    source = serializers.SlugRelatedField(
        queryset=Airport.objects.all(), slug_field="name"
    )
    destination = serializers.SlugRelatedField(
        queryset=Airport.objects.all(), slug_field="name"
    )

    class Meta:
        model = Route
        fields = (
            "id",
            "source",
            "destination",
            "distance",
        )
        read_only_fields = ("id",)
