from django.conf import settings
from django.db import models

class UserProfile(models.Model):
    """
    A unified UserProfile model that handles both CareGiver and EndUser roles,
    with specific fields and relationships based on role.
    """

    # Role choices
    USER_ROLES = (
        ('CG', 'CareGiver'),  # Caregivers who manage and assist EndUsers
        ('EU', 'EndUser'),     # EndUsers who receive assistance from CareGivers
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)               # Common for both roles
    email = models.EmailField(unique=True)                # Common for both roles
    role = models.CharField(max_length=2, choices=USER_ROLES, default='EU')  # Role identifier
    about = models.TextField(blank=True, null=True)       # Common for both roles
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation

     # Foreign key for end users linked to a caregiver
    caregiver = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True,
        related_name='end_users',
        limit_choices_to={'role': 'CG'}
    )

    def __str__(self):
        return f"{self.name} ({self.get_role_display()})"

