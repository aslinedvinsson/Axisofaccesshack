from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseForbidden
from .models import Icon, Notification
from accounts.models import UserProfile

def send_notification(request, icon_id):
    """
    Sends a notification to the caregiver when an end user selects an icon.
    """
    user = request.user

    # Check if the user is an end user
    if not hasattr(user, 'userprofile') or user.userprofile.role != 'EU':
        return JsonResponse({'error': 'Only end users can select icons.'}, status=403)

    # Get the icon and ensure it's active
    icon = get_object_or_404(Icon, id=icon_id, is_active=True)

    # Get the caregiver associated with the icon
    caregiver = icon.caregiver

    if not caregiver:
        return JsonResponse({'error': 'This icon is not associated with a caregiver.'}, status=404)

    # Create a notification for the caregiver
    Notification.objects.create(
        caregiver=caregiver,
        user=user.userprofile,
        icon=icon,
        is_sent=True
    )

    return JsonResponse({'message': f'Notification sent to {caregiver.name} for icon: {icon.name}'})



