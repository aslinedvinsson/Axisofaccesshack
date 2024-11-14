from django.urls import path
from . import views

urlpatterns = [
    path('user_profile', views.user_profile, name='user_profile'),
    path('caregiver_profile', views.caregiver_profile, name='caregiver_profile'),
]