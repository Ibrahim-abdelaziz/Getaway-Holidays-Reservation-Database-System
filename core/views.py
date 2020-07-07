from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, GenericAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions 
from .models.reservation import Reservation
from .models.accommodation import Accommodation
from .models.activity import Activity
from .models.supervisor import Supervisor
from .models.supplier import Supplier
from .models.equipment import Equipment
from . import serializers


# Create your views here.

class ReservationView(ModelViewSet):
    queryset           = Reservation.objects.all()
    serializer_class   = serializers.ReservationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return serializers.ReservationSerializerPost
        return serializers.ReservationSerializer

    def get_queryset(self):
        query = super().get_queryset()

        if self.request.user:
            query = Reservation.objects.filter(client=self.request.user.id)

        return query



class AccommodationView(ModelViewSet):
    queryset           = Accommodation.objects.all()
    serializer_class   = serializers.AccommodationnSerializer
    permission_classes = (permissions.IsAuthenticated,)
    http_method_names  = ['get']



class ActivityView(ModelViewSet):
    queryset           = Activity.objects.all()
    serializer_class   = serializers.ActivitySerializer
    permission_classes = (permissions.IsAuthenticated,)
    http_method_names  = ['get']





