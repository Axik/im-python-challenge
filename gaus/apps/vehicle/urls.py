from django.conf.urls import patterns, url

urlpatterns = patterns(
    'vehicle.views',
    url(r'^(?P<pk>\d+)$', 'vehicle_retrieve', name='retrieve'),
    url(r'^price$', 'vehicle_list', name='list')
)
