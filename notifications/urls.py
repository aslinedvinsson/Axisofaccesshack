from django.urls import path
from .views import  send_notification, notification_index, unread_notification_count

urlpatterns = [
    path('notifications/', notification_index, name='notification_index'),
    path('send-notification/<int:icon_id>/', send_notification, name='send_notification'),
    path('unread_notifications/', unread_notification_count, name='unread_notifications'),
]


