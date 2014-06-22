from dateutil import parser

from django.shortcuts import get_object_or_404
from django.db.models import Q

from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import VehicleProspects
from .serializers import VehicleProspectsSerializer


class VehicleReadOnlyModelViewSet(ReadOnlyModelViewSet):
    model = VehicleProspects
    serializer_class = VehicleProspectsSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(self.model, **{'id': pk})

    def get_queryset(self, queryset=None):
        params = self.request.GET
        dates = dict(post_date__gte=params.get('postedFrom'),
                     post_date__lte=params.get('postedTo'))
        for k, v in dates.items():
            try:
                dates[k] = parser.parse(v)
            except Exception:
                dates[k] = None
        search = dict(make=params.get('make'),
                      title__icontains=params.get('title'),
                      mileage__gte=params.get('mileageFrom'),
                      mileage__lte=params.get('mileageTo'))
        search.update(dates)
        query = Q()
        for parameter_name, value in search.items():
                    if value:
                        query &= Q(**{parameter_name: value})
        return self.model.objects.filter(query)


vehicle_list = VehicleReadOnlyModelViewSet.as_view({'get': 'list'})
vehicle_retrieve = VehicleReadOnlyModelViewSet.as_view({'get': 'retrieve'})
