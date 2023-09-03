from django.db import models


class DeliveryPersonnel(models.Model):
    name = models.CharField(max_length=255)
    vehicle = models.CharField(max_length=255)

    def __str__(self):
        return self.name
