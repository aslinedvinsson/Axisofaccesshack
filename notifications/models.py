from django.db import models
from accounts.models import UserProfile
from communication.models import Group, Icon

# Create your models here.
class Notification(models.Model):
    """
    Represents a notification sent by a caregiver to a user, associated with an icon.
    """
    caregiver = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="sent_notifications",
        limit_choices_to={'role': 'CG'}
    )
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="received_notifications"
    )
    icon = models.ForeignKey(
        Icon, on_delete=models.CASCADE, related_name="notifications"
    )
    notified_at = models.DateTimeField(auto_now_add=True)
    is_sent = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification from {self.caregiver} to {self.user} - {self.icon.name}"