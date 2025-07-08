from django.db import models


class Route(models.Model):
    source = models.ForeignKey(
        "flights.Airport",
        on_delete=models.CASCADE,
        related_name="sources"
    )
    destination = models.ForeignKey(
        "flights.Airport",
        on_delete=models.CASCADE,
        related_name="destinations"
    )
    distance = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.source}-{self.destination}"
