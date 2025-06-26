from django.core.exceptions import ValidationError
from django.db import models

from flights.models import Airplane, Flight, Order


class Ticket(models.Model):
    row = models.PositiveIntegerField()
    seat = models.PositiveIntegerField()
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="tickets")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="tickets")

    def __str__(self):
        return f"Ticket {self.row}-{self.seat} on {self.flight}"

    def clean(self):
        airplane = self.flight.airplane
        if self.row > airplane.rows or self.seat > airplane.seats_in_row:
            raise ValidationError("Seat number is out of range for this airplane.")

    class Meta:
        unique_together = [["flight", "row", "seat"]]
