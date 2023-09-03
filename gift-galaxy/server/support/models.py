from django.db import models


class SupportMessage(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Support Message {self.id} - {self.user.username}'
