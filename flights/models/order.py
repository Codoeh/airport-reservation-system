from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")

    def __str__(self):
        return f"Order #{self.id} by {self.user.username} at {self.created_at}"

    class Meta:
        ordering = ["-created_at"]
