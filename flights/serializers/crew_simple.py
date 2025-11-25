from rest_framework import serializers

from flights.models.crew import Crew


class CrewSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crew
        fields = (
            "id",
            "first_name",
            "last_name",
        )
