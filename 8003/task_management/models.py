from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    due_date = models.DateField()
    user = models.ForeignKey('user_management.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
