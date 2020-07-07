from django.contrib import admin
from core.models.reservation import Reservation
from core.models.accommodation import Accommodation
from core.models.activity import Activity
from core.models.supervisor import Supervisor
from core.models.supplier import Supplier
from core.models.equipment import Equipment


# Register your models here.
admin.site.register(Reservation)
admin.site.register(Accommodation)
admin.site.register(Activity)
admin.site.register(Supervisor)
admin.site.register(Supplier)
admin.site.register(Equipment)

