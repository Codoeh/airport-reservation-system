from rest_framework import serializers

from .airplane import AirplaneSerializer
from .crew_simple import CrewSimpleSerializer
from .route import RouteSerializer
from ..models.flight import Flight


class FlightSerializer(serializers.ModelSerializer):
    crew = CrewSimpleSerializer(many=True, read_only=True)
    route = RouteSerializer(many=False, read_only=True)
    airplane = AirplaneSerializer(many=False, read_only=True)
    taken_seats = serializers.SerializerMethodField()

    class Meta:
        model = Flight
        fields = (
            "id",
            "departure_time",
            "arrival_time",
            "crew",
            "route",
            "airplane",
            "taken_seats",
        )

    def get_taken_seats(self, obj):
        return [
            (f"Row: {ticket.row}, seat: {ticket.seat}, "
             f"seat_nr: {(ticket.row - 1) * 10 + ticket.seat}")
            for ticket in obj.tickets.all()
        ]


class FlightInCrewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ("id",)


class FlightInCrewDetailSerializer(serializers.ModelSerializer):
    route = serializers.StringRelatedField()
    airplane = serializers.StringRelatedField()

    class Meta:
        model = Flight
        fields = (
            "id",
            "departure_time",
            "arrival_time",
            "route",
            "airplane",
        )


class FlightListSerializer(serializers.ModelSerializer):
    crew = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    route = serializers.PrimaryKeyRelatedField(read_only=True)
    airplane = serializers.PrimaryKeyRelatedField(read_only=True)
    tickets_available = serializers.SerializerMethodField()

    class Meta:
        model = Flight
        fields = (
            "id",
            "departure_time",
            "arrival_time",
            "route",
            "airplane",
            "crew",
            "tickets_available",
        )

    def get_tickets_available(self, obj):
        total_seats = obj.airplane.rows * obj.airplane.seats_in_row
        taken_seats = obj.tickets.count()
        return total_seats - taken_seats


class FlightInOrdersSerializer(FlightListSerializer):
    source = serializers.PrimaryKeyRelatedField(
        read_only=True, source="route.source.name"
    )
    destination = serializers.PrimaryKeyRelatedField(
        read_only=True, source="route.destination.name"
    )
    airplane = serializers.PrimaryKeyRelatedField(
        read_only=True, source="airplane.name"
    )
    tickets_available = serializers.SerializerMethodField()

    class Meta:
        model = Flight
        fields = (
            "id",
            "departure_time",
            "arrival_time",
            "source",
            "destination",
            "airplane",
        )


class FlightInOrdersDetailSerializer(FlightListSerializer):
    source = serializers.PrimaryKeyRelatedField(
        read_only=True, source="route.source.name"
    )
    destination = serializers.PrimaryKeyRelatedField(
        read_only=True, source="route.destination.name"
    )
    airplane = serializers.PrimaryKeyRelatedField(
        read_only=True, source="airplane.name"
    )
    tickets_available = serializers.SerializerMethodField()

    class Meta:
        model = Flight
        fields = (
            "id",
            "departure_time",
            "arrival_time",
            "source",
            "destination",
            "airplane",
        )
