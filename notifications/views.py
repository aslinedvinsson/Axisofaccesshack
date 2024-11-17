from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseForbidden
from django.utils.timezone import now
from datetime import timedelta
from .models import Icon, Notification
from accounts.models import UserProfile

def notification_index(request):
    """
    Displays notifications for the logged-in caregiver.
    """
    try:
        caregiver_profile = request.user.userprofile
        if caregiver_profile.role != 'CG':
            return JsonResponse({'error': 'Only caregivers can view notifications.'}, status=403)
    except AttributeError:
        return JsonResponse({'error': 'User profile not found.'}, status=403)

    # Fetch notifications for this caregiver
    notifications = Notification.objects.filter(caregiver=caregiver_profile).order_by('-notified_at')
    
    # Add human-readable time to each notification
    for notification in notifications:
        notification.time_since = time_since(notification.notified_at)

    # Mark all notifications as viewed
    Notification.objects.filter(caregiver=caregiver_profile, is_viewed=False).update(is_viewed=True)

    # Fetch distinct end-users directly from the caregiver's profile
    assigned_endusers = caregiver_profile.end_users.values_list('name', flat=True).distinct()

    return render(request, 'notificationindex.html', {
        'notifications': notifications,
        'assigned_endusers': assigned_endusers,
    })


def time_since(notification_time):
    """
    Returns a human-readable string for time differences.
    """
    diff = now() - notification_time
    seconds = diff.total_seconds()
    if seconds < 60:
        return "less than a minute ago"
    elif seconds < 3600:
        return f"{int(seconds // 60)} minutes ago"
    elif seconds < 86400:
        return f"{int(seconds // 3600)} hours ago"
    else:
        days = int(seconds // 86400)
        return f"{days} day{'s' if days > 1 else ''} ago"

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


def unread_notification_count(request):
    if request.user.is_authenticated and hasattr(request.user, 'userprofile') and request.user.userprofile.role == 'CG':
        unread_count = Notification.objects.filter(caregiver=request.user.userprofile, is_viewed=False).count()
        return JsonResponse({'unread_count': unread_count})
    return JsonResponse({'error': 'Unauthorized'}, status=403)


def delete_notification(request, notification_id):
    if request.method == "POST" and request.user.is_authenticated:
        # Get the notification and ensure it belongs to the user
        notification = get_object_or_404(Notification, id=notification_id, caregiver=request.user.userprofile)
        notification.delete()
        return JsonResponse({"success": True, "message": "Notification deleted successfully."})
    return JsonResponse({"success": False, "message": "Invalid request."}, status=400)