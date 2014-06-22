from rest_framework import serializers

from .models import VehicleProspects


class VehicleProspectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = VehicleProspects
        fields = fields = ['price', 'mileage', 'make']
