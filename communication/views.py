from django.shortcuts import render
from .models import Group, Icon

def index(request):
    user_role = None
    groups, icons, favorites = None, None, None

    if request.user.is_authenticated and hasattr(request.user, 'userprofile'):
        user_role = request.user.userprofile.role

        if user_role == 'EU':  # EndUser role
            groups = Group.objects.prefetch_related('icons').all()
            for group in groups:
                group.active_icons = group.icons.filter(is_active=True)  # Only active icons
            icons = Icon.objects.filter(is_active=True).order_by('name')
            favorites = Icon.objects.filter(
                is_favorite=True, is_active=True, caregiver__user=request.user
            ).order_by('name')
        elif user_role == 'CG':  # CareGiver role
            # Caregivers can view groups and icons, but no interaction
            groups = Group.objects.prefetch_related('icons').all()
            for group in groups:
                group.active_icons = group.icons.filter(is_active=True)  # Only active icons
            icons = Icon.objects.filter(is_active=True).order_by('name')
            favorites = Icon.objects.none()  # CareGivers do not have favorites
    else:
        # Unauthenticated users see default icons only
        icons = Icon.objects.filter(is_default=True, is_active=True).order_by('name')

    return render(request, 'communication/index.html', {
        'groups': groups,
        'icons': icons,
        'favorites': favorites,
        'user_role': user_role,
    })


# View to display custom 404 page
def custom_404(request, exception):
    return render(request, '404.html', status=404)