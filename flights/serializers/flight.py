from rest_framework import serializers

from .airplane import AirplaneSerializer
from .crew_simple import CrewSimpleSerializer
from .route import RouteSerializer
from ..models.flight import Flight


class FlightSerializer(serializers.ModelSerializer):
    crew = CrewSimpleSerializer(many=True, read_only=True)
    route = RouteSerializer(many=False, read_only=True)
    airplane = AirplaneSerializer(many=False, read_only=True)

    class Meta:
        model = Flight
        fields = (
            "id",
            "departure_time",
            "arrival_time",
            "crew",
            "route",
            "airplane",
        )
