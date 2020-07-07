from djmoney.models.fields import MoneyField
from django.db import models
from djmoney.money import Money
from djmoney.contrib.exchange.models import convert_money
from django.contrib.auth.models import User
from .activity import Activity
import datetime
from django.db.models import Count


class Reservation(models.Model):
    client            = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_reservation')
    accommodation     = models.ForeignKey('core.Accommodation', related_name='reservation_accommodation', on_delete=models.CASCADE)
    activity          = models.ManyToManyField('core.Activity', related_name='reservation_activity')
    reservation_date  = models.DateTimeField(auto_now_add=True)
    start_trip        = models.DateTimeField()
    end_trip          = models.DateTimeField()
    no_of_guest       = models.IntegerField()
    no_of_room        = models.IntegerField()
    trip_discount     = models.FloatField(default=0)
    client_signature  = models.CharField(max_length=50, null=True, blank=True)
    client_date       = models.DateField(null=True, blank=True)
    agent_signature   = models.CharField(max_length=50, null=True, blank=True)
    agent_date        = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.client)


    # This Function to Display Activity_detail
    @property
    def activity_detail(self):

        activites_info = self.activity.all().prefetch_related('reservation_activity')
        return str(activites_info)


   # This Function to calculate cost_of_trip
    @property
    def cost_of_trip(self):

        try:
            
            activites = self.activity.all().prefetch_related('reservation_activity')
            activites_sum = activites.aggregate(models.Sum('activity_cost')).get('activity_cost__sum')
            result = activites_sum +  self.accommodation.room_rate.amount
            return result

        except Exception:
            return 0


    # This Function to calculate Activity_discount
    @property
    def activity_discounts(self):

        try:
            act_count = self.activity.filter(kind_of_activity='outdoor').count()
            activites = self.activity.filter(kind_of_activity='outdoor').prefetch_related('reservation_activity')
            activites_sum = activites.aggregate(models.Sum('activity_cost')).get('activity_cost__sum') 

            if act_count > 2 :                
                return float(activites_sum) * (15 / 100)
            return 0
            
        except Exception:
            return 0


    # This Function to calculate discount_on_two_trip_in_the_same_year
    @property
    def discount_on_two_trip_in_the_same_year(self):
        qs = Reservation.objects.filter(client=self.client, reservation_date__year="2020").count()
        if qs == 2:
            query = Reservation.objects.filter(client=self.client, reservation_date__year="2020")[1]
            query.trip_discount = float(query.cost_of_trip) * (10 / 100)
            query.save()

            return self.trip_discount
        return 0


