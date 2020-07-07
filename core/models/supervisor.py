from django.db import models
from django.contrib.auth.models import User
from .activity import Activity


class Supervisor(models.Model):
    types = (
        ('masseuse', 'masseuse'),
        ('outdoor_instructor', 'outdoor_instructor'),
        ('swim_instructor', 'swim_instructor')
    )
    name               = models.CharField(max_length=50)
    qualification      = models.CharField(max_length=255)
    field_of_expertise = models.CharField(max_length=50)
    address            = models.CharField(max_length=255)
    contact            = models.CharField(max_length=50)
    work_schedule      = models.CharField(max_length=255)
    type_supervisor    = models.CharField(max_length=50, choices=types)
    data_supervisor    = models.DateTimeField()
    activity           = models.ForeignKey("Activity", related_name='supervisor', on_delete=models.CASCADE)


    def __str__(self):
        return self.name