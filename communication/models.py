from django.db import models
from accounts.models import UserProfile

class Group(models.Model):
    """
    Represents a category or grouping of icons, such as "Basic Needs" or "Emotions".
    """
    name = models.CharField(max_length=50, unique=True)  # Ensures each group name is unique
    description = models.TextField(blank=True, null=True)  # Optional description of the group

    def __str__(self):
        return self.name

class Icon(models.Model):
    """
    Represents an icon that an end user can use to communicate with a caregiver.
    Icons are created and managed by caregivers and can be grouped for easier navigation.
    """
    caregiver = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="icons",
        limit_choices_to={'role': 'CG'},  # Only caregivers can own icons
        null=True,  # Allows this field to be empty for default icons
        blank=True
    )
    name = models.CharField(max_length=100)  # Name of the icon, e.g., "Hungry", "Thirsty"
    image = models.ImageField(upload_to="icons/")  # Icon image file upload
    is_default = models.BooleanField(default=False)  # Marks if the icon is a system default
    is_active = models.BooleanField(default=True)    # Allows caregivers to hide/unhide icons
    is_favorite = models.BooleanField(default=False)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, related_name="icons") # ForeignKey to group

    def __str__(self):
        return self.name