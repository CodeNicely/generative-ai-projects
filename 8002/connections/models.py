from django.db import models
from users.models import UserProfile


class Connection(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='connections')
    connected_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='connected_users')
    access_level = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.connected_user.username}'
