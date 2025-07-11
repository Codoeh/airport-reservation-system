from rest_framework import serializers

from .flight import (
    FlightSerializer,
    FlightInCrewListSerializer,
    FlightInCrewDetailSerializer,
)
from ..models import Flight
from ..models.crew import Crew


class CrewSerializer(serializers.ModelSerializer):
    flights = FlightSerializer(many=True, read_only=True)
    flights_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Flight.objects.all(),
        write_only=True,
        source="flights"
    )

    class Meta:
        model = Crew
        fields = (
            "id",
            "first_name",
            "last_name",
            "flights",
            "flights_ids",
        )
        read_only_fields = ("id",)


class CrewListSerializer(CrewSerializer):
    flights = FlightInCrewListSerializer(many=True, read_only=True)


class CrewDetailSerializer(CrewSerializer):
    flights = FlightInCrewDetailSerializer(many=True, read_only=True)
