from djmoney.models.fields import MoneyField
from django.db import models
from djmoney.money import Money

from django.contrib.auth.models import User





class Accommodation(models.Model):
    types = (
        ('deluxe_cottage', 'deluxe_cottage'),
        ('honeymoon_cottage', 'honeymoon_cottage'),
        ('double_bed', 'double_bed'),
        ('single_bed', 'single_bed')
    )
    room_type        = models.CharField(max_length=50, choices=types)
    room_rate        = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    room_connectiong = models.BooleanField(default=False)
    floor_level      = models.CharField(max_length=50, null=True)


    def __str__(self):
        return self.room_type