from django.db import models


class Lease(models.Model):
    property_id = models.ForeignKey('properties.Property', on_delete=models.CASCADE)
    tenant_id = models.ForeignKey('users.User', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'Lease #{self.id}'
