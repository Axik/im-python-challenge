from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import VehicleProspects


class VehicleReadOnlyModelViewSet(ReadOnlyModelViewSet):
    model = VehicleProspects

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(self.model, **{'id': pk})


vehicle_list = VehicleReadOnlyModelViewSet.as_view({'get': 'list'})
vehicle_retrieve = VehicleReadOnlyModelViewSet.as_view({'get': 'retrieve'})
