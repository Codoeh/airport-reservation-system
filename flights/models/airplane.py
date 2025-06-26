from django.core.exceptions import ValidationError
from django.db import models


class Airplane(models.Model):
    name = models.CharField(max_length=255, unique=True)
    rows = models.PositiveIntegerField()
    seats_in_row = models.PositiveIntegerField()
    airplane_type = models.ForeignKey("flights.AirplaneType", on_delete=models.CASCADE, related_name="airplanes")

    def clean(self):
        if self.rows <= 0 or self.seats_in_row <= 0:
            raise ValidationError("Number of rows and seats in row must be higher than 0.")

    @property
    def total_seats(self):
        return self.rows * self.seats_in_row

    def __str__(self):
        return f"{self.airplane_type}: {self.name}. Total seats: {self.total_seats}."
