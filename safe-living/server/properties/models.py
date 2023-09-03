from django.db import models
from users.models import User


class Property(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.IntegerField()
    location = models.CharField(max_length=255)
    amenities = models.CharField(max_length=255)
    landlord = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
