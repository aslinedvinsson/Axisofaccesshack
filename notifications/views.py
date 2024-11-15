from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseForbidden
from .models import Icon, Notification
from accounts.models import UserProfile

def notification_index(request):
    """
    Displays a list of icons for caregivers.
    """
    user = request.user

    # Ensure only authenticated users can access
    if not user.is_authenticated:
        return redirect('account_login')

    # Ensure only caregivers can access
    if not hasattr(user, 'userprofile') or user.userprofile.role != 'CG':
        return HttpResponseForbidden("You do not have permission to view this page.")

    # Fetch active icons
    icons = Icon.objects.filter(is_active=True)

    return render(request, 'notificationindex.html', {'icons': icons})


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



