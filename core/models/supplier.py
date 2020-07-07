from django.db import models
from django.contrib.auth.models import User





class Supplier(models.Model):
    bill_coder            = models.IntegerField()
    bussiness_name        = models.CharField(max_length=255)
    contact_person_detail = models.CharField(max_length=255)
    supplier_contact      = models.CharField(max_length=255)
    
     

    def __str__(self):
        return self.supplier_contact