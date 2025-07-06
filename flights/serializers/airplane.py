from rest_framework import serializers

from ..models.airplane import Airplane


class AirplaneSerializer(serializers.ModelSerializer):
    airplane_type_name = serializers.CharField(
        source="airplane_type.name", read_only=True
    )

    class Meta:
        model = Airplane
        fields = (
            "id",
            "name",
            "rows",
            "seats_in_row",
            "airplane_type",
            "airplane_type_name",
        )
        read_only_fields = ("id",)
