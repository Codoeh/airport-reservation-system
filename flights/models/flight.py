from django.db import models


class Flight(models.Model):
    route = models.ForeignKey("flights.Route", on_delete=models.CASCADE, related_name="flights")
    airplane = models.ForeignKey("flights.Airplane", on_delete=models.CASCADE, related_name="flights")
    departure_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    arrival_time = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return (f"From - to: {self.route}. "
                f"Plane: {self.airplane}. "
                f"Departure time - arrival time: {self.departure_time} - {self.arrival_time}")
