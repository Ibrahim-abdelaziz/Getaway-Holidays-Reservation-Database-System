from django.contrib import admin
from accounts.model.client import Client
from accounts.model.address import Address

# Register your models here.


admin.site.register(Client)
admin.site.register(Address)
