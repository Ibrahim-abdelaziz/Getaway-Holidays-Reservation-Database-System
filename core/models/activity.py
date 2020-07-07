from djmoney.models.fields import MoneyField
from django.db import models
from djmoney.money import Money
from django.contrib.auth.models import User



class Activity(models.Model):
    type_risk = (
        ('low', 'low'),
        ('medium', 'medium'),
        ('high', 'high')
    )
    type_activity = (
        ('indoor', 'indoor'),
        ('outdoor', 'outdoor'),
    )
    
    kind_of_activity     = models.CharField(max_length=50, choices=type_activity)
    activity_describtion = models.TextField()
    risk_level           = models.CharField(max_length=50, choices=type_risk)
    activity_cost        = MoneyField(max_digits=14, decimal_places=2, default_currency='AUD')



    def __str__(self):
        return f'{self.activity_describtion} -- {self.activity_cost}'