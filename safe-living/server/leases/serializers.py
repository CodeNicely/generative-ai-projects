from rest_framework import serializers
from .models import Lease


class LeaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lease
        fields = ['id', 'property', 'tenant', 'start_date', 'end_date']
