from django.db import models


class Crew(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    flights = models.ManyToManyField("flights.Flight", blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
