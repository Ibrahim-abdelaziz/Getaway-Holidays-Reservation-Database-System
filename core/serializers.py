from .models.reservation import Reservation
from .models.accommodation import Accommodation
from .models.activity import Activity
from .models.supervisor import Supervisor
from .models.supplier import Supplier
from .models.equipment import Equipment
from django.contrib.auth.models import User
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
import datetime
from datetime import datetime, timezone 



class AccommodationnSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Accommodation
        fields = "__all__"
        

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Activity
        fields = "__all__"
        

class ReservationSerializerPost(WritableNestedModelSerializer):

    class Meta:
        model  = Reservation
        fields = "__all__"
    

class ReservationSerializer(serializers.ModelSerializer):
    client_detail               = serializers.SerializerMethodField()
    accommodation_detail        = serializers.SerializerMethodField()
    duration_trip               = serializers.SerializerMethodField()
    trip_dicount_exceeds_5_days = serializers.SerializerMethodField()
    net_of_trip                 = serializers.SerializerMethodField()
      
    
    def get_client_detail(self, obj):
        if obj.client:
            return obj.client.username


    def get_accommodation_detail(self, obj):
        if obj.accommodation:
            return ({"accommodation_type":obj.accommodation.room_type, "accommodation_cost":obj.accommodation.room_rate.amount})


    def get_duration_trip(self, obj):
        try:
            start_date = obj.start_trip
            end_date = obj.end_trip
            date = end_date - start_date
            request = self.context.get('request')
            return date.days 

        except:
            return 0


    def get_trip_dicount_exceeds_5_days(self, obj):
        try:
            days = self.get_duration_trip(obj)
            if days > 5:
                return obj.cost_of_trip * 5 / 100
            return 0

        except Exception:
            return 0


    def get_net_of_trip(self, obj):
        return float(obj.cost_of_trip) - obj.activity_discounts - float(self.get_trip_dicount_exceeds_5_days(obj)) - obj.discount_on_two_trip_in_the_same_year

    class Meta:
        model  = Reservation
        fields = ('id', 'client_detail','accommodation_detail', 'activity_detail', 'reservation_date', 'start_trip', 'end_trip', 'duration_trip', 'no_of_guest', 'no_of_room', 'cost_of_trip', 'activity_discounts', 'trip_dicount_exceeds_5_days', 'discount_on_two_trip_in_the_same_year','net_of_trip')


class SupervisorSerializer(serializers.ModelSerializer):
    activity_detail = serializers.SerializerMethodField(required=False)

    def get_activity(self, obj):
        if obj.activity:
            return obj.activity.kind_of_activity

    class Meta:
        model  = Supervisor
        fields = "__all__"
        

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Supplier
        fields = "__all__"
        

class EquipmentSerializer(serializers.ModelSerializer):
    supplier_detail = serializers.SerializerMethodField(required=False)

    def get_supplier_detail(self, obj):
        if obj.supplier:
            return obj.supplier.contact_person_detail
        
    class Meta:
        model  = Equipment
        fields = "__all__"