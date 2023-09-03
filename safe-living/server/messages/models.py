from django.db import models


class Message(models.Model):
    sender_id = models.ForeignKey('users.User', on_delete=models.CASCADE)
    receiver_id = models.ForeignKey('users.User', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message #{self.id}'
