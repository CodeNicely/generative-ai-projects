from django.db import models


class MaintenanceRequest(models.Model):
    property_id = models.ForeignKey('properties.Property', on_delete=models.CASCADE)
    tenant_id = models.ForeignKey('users.User', on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=255)

    def __str__(self):
        return f'Maintenance Request #{self.id}'
