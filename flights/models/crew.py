from django.db import models

from flights.models import Flight


class Crew(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    flights = models.ManyToManyField(Flight)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
