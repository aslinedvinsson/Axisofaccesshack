from django.urls import path
from .views import  send_notification, notification_index

urlpatterns = [
    path('notifications/', notification_index, name='notification_index'),
    path('send-notification/<int:icon_id>/', send_notification, name='send_notification'),
]


