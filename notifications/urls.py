from django.urls import path
from .views import  send_notification

urlpatterns = [
    path('send-notification/<int:icon_id>/', send_notification, name='send_notification'),
]


