# attachments/models.py

from django.db import models
from expenses.models import Expense


class Attachment(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    file_path = models.CharField(max_length=255)

    def __str__(self):
        return f'Attachment {self.id}'
