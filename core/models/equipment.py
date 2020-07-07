from django.db import models
from django.contrib.auth.models import User
from .activity import Activity
from .supplier import Supplier


class Equipment(models.Model):
    equip_info      = models.TextField()
    equip_count     = models.IntegerField()
    inspection_date = models.DateField(null=True, blank=True)
    activity        = models.ForeignKey(Activity, related_name='equipment_activity', on_delete=models.CASCADE)
    supplier         = models.ForeignKey(Supplier, related_name='equipment', on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.equip_info