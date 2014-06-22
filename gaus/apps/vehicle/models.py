from django.db import models
from django.utils.translation import ugettext_lazy as _


class VehicleProspects(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, blank=True)
    year = models.CharField(max_length=255, blank=True)
    make = models.CharField(max_length=255, blank=True)
    price = models.IntegerField(blank=True, null=True)
    mileage = models.IntegerField(blank=True, null=True)
    post_date = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True)
    href = models.TextField(blank=True)
    email = models.TextField(blank=True)
    post_text = models.TextField(blank=True)
    unique_digest = models.CharField(unique=True, max_length=255, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    origin = models.CharField(max_length=255, blank=True)
    listing_id = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    active = models.IntegerField(blank=True, null=True)
    vin = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'vehicle_prospects'
        verbose_name = _('Vehicle Prospect')
        verbose_name_plural = _('Vehicle Prospects')

    def __str__(self):
        return '{} #{}'.format(self.title, self.id)
