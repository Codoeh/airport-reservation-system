from rest_framework import serializers

from ..models.crew import Crew


class CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crew
        fields = (
            "id",
            "first_name",
            "last_name",
            "flights",
        )
        read_only_fields = ("id",)
