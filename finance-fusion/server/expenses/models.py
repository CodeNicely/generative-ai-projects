# expenses/models.py

from django.db import models


class Expense(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    description = models.TextField()
    payment_method = models.CharField(max_length=255)

    def __str__(self):
        return f'Expense {self.id}'
