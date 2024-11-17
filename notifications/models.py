from django.db import models
from accounts.models import UserProfile
from communication.models import Icon

class Notification(models.Model):
    """
    Represents a notification sent to a caregiver when an event (e.g., icon selection) occurs.
    """
    caregiver = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="notifications",
        limit_choices_to={'role': 'CG'},  # Ensure only caregivers receive notifications
        help_text="The caregiver receiving the notification."
    )
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="user_notifications",
        limit_choices_to={'role': 'EU'},
        help_text="The user who triggered the notification."
    )
    icon = models.ForeignKey(
        Icon,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="notifications",
        help_text="The icon selected by the user."
    )
    notified_at = models.DateTimeField(
        auto_now_add=True,
        help_text="The time when the notification was created."
    )
    is_sent = models.BooleanField(
        default=False,
        help_text="Whether the notification has been sent."
    )
    is_viewed = models.BooleanField(
        default=False,
        help_text="Whether the notification has been viewed."
    )

    def __str__(self):
        return f"Notification to {self.caregiver} about {self.icon.name if self.icon else 'N/A'}"
