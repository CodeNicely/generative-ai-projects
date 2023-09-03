from rest_framework import serializers
from .models import DeliveryPersonnel


class DeliveryPersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryPersonnel
        fields = ['id', 'name', 'vehicle']
