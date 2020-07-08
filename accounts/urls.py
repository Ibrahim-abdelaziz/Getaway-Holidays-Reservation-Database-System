from django.urls import path, include
from django.views.generic import TemplateView
from rest_auth.views import (
                            LoginView, PasswordResetView,
                            PasswordResetConfirmView, PasswordChangeView,
                            LogoutView
                            )
from rest_auth.registration.views import RegisterView, VerifyEmailView
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('client', views.ClientView)

urlpatterns = [
    path('', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('login/', LoginView.as_view(), name='account_login'),
    path('logout/', LogoutView.as_view(), name='rest_logout'),
    path('accounts/', include('allauth.urls')),
    path('delete-account/', views.DeleteAccount.as_view()),

]
