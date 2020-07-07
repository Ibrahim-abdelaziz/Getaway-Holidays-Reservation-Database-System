from django.db import models




class Address(models.Model):
    Postcode         = models.CharField(max_length=10)
    City             = models.CharField(max_length=50)
    State            = models.CharField(max_length=50)


    def __str__(self):
        return self.City