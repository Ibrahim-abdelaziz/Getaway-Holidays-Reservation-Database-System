
from django.db import models
from django.contrib.auth.models import User
from accounts.model.address import Address
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime


class Client(models.Model):
    user             = models.OneToOneField(User, related_name='client', on_delete=models.CASCADE) 
    Client_name      = models.CharField(max_length=50)
    Address          = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='client_adress', null=True, blank=True)
    Date_of_birth    = models.DateField(null=True,blank=True)
    Contact_number   = models.CharField(max_length=50, null=True, blank=True)
    Occupation       = models.CharField(max_length=50, null=True, blank=True)
    Marital_status   = models.CharField(max_length=50, null=True, blank=True)
    Anniversary      = models.DateField(null=True, blank=True)
    Blood_pressure   = models.BooleanField(default=False)
    Heart_condition  = models.BooleanField(default=False)
    Photophobia      = models.BooleanField(default=False)
    Acrophobia       = models.BooleanField(default=False)


    def __str__(self):
        return str(self.user)

    def save(self, *args, **Kwargs):
        if self.user:
            self.Client_name = self.user
        super(Client, self).save(*args, **Kwargs)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, *args, **kwargs):
    if created:
        Client.objects.create(user=instance)

