from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('reservation', views.ReservationView)
router.register('accommodation', views.AccommodationView)
router.register('activity', views.ActivityView)


urlpatterns = [
  path('', include(router.urls)),


]
