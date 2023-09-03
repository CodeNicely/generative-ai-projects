from django.db import models
from users.models import User
from properties.models import Property


class Booking(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    tenant = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)

    def __str__(self):
        return f'Booking #{self.id}'
