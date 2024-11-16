from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseForbidden
from .models import Icon, Notification
from accounts.models import UserProfile

def notification_index(request):
    """
    Displays notifications for the logged-in caregiver.
    """
    # Check if the logged-in user has a UserProfile and is a caregiver
    try:
        caregiver_profile = request.user.userprofile
        if caregiver_profile.role != 'CG':
            return JsonResponse({'error': 'Only caregivers can view notifications.'}, status=403)
    except AttributeError:
        return JsonResponse({'error': 'User profile not found.'}, status=403)

    # Get notifications for this caregiver
    notifications = Notification.objects.filter(caregiver=caregiver_profile).order_by('-notified_at')

    return render(request, 'notificationindex.html', {'notifications': notifications})


def send_notification(request, icon_id):
    """
    Sends a notification to the caregiver when an end user selects an icon.
    """
    # Get the UserProfile for the logged-in user
    user_profile = getattr(request.user, 'userprofile', None)

    # Validate that the user has a UserProfile and is an end user
    if not user_profile or user_profile.role != 'EU':
        return JsonResponse({'error': 'Only end users can select icons.'}, status=403)

    # Get the icon and validate that it is active
    icon = get_object_or_404(Icon, id=icon_id, is_active=True)

    # Get the caregiver associated with the icon
    caregiver = icon.caregiver
    if not caregiver:
        return JsonResponse({'error': 'This icon is not associated with a caregiver.'}, status=404)

    # Create a notification for the caregiver
    Notification.objects.create(
        caregiver=caregiver,
        user=user_profile,  # Populate user field with the end user's profile
        icon=icon,
        is_sent=True
    )

    return JsonResponse({'message': f'Notification sent to {caregiver.name} for icon: {icon.name}'})