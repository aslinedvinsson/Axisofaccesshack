from django.urls import path
from . import views


urlpatterns = [
    path(
      'notifications/',
      views.notification_index,
      name='notification_index'
    ),
    path(
      'send-notification/<int:icon_id>/',
      views.send_notification,
      name='send_notification'
    ),
    path(
      'unread_notifications/',
      views.unread_notification_count,
      name='unread_notifications'
    ),
    path(
      "delete_notification/<int:notification_id>/",
      views.delete_notification,
      name="delete_notification"
    ),
]
