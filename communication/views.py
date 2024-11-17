from django.shortcuts import render
from .models import Group, Icon


def index(request):
    user_role = None
    groups, icons, favorites = None, None, None

    if request.user.is_authenticated and hasattr(request.user, 'userprofile'):
        user_role = request.user.userprofile.role

        if user_role == 'EU':  # EndUser role
            # Fetch the caregiver assigned to this end user
            caregiver = request.user.userprofile.caregiver

            if caregiver:
                # Retrieve icons favorited by the assigned caregiver
                favorites = Icon.objects.filter(
                    caregiver=caregiver,
                    is_favorite=True,
                    is_active=True
                ).order_by('name')
            else:
                # If no caregiver is assigned, no favorites are shown
                favorites = Icon.objects.none()

            groups = Group.objects.prefetch_related('icons').all()
            for group in groups:
                # Only active icons
                group.active_icons = group.icons.filter(is_active=True)
            icons = Icon.objects.filter(is_active=True).order_by('name')

        elif user_role == 'CG':  # CareGiver role
            groups = Group.objects.prefetch_related('icons').all()
            for group in groups:
                # Only active icons
                group.active_icons = group.icons.filter(is_active=True)
            icons = Icon.objects.filter(is_active=True).order_by('name')

            # Include favorites selected by the caregiver
            favorites = Icon.objects.filter(
                is_favorite=True,
                is_active=True,
                caregiver=request.user.userprofile
            ).order_by('name')
    else:
        # Unauthenticated users see default icons only
        icons = Icon.objects.filter(
            is_default=True, is_active=True
        ).order_by('name')

    return render(request, 'communication/index.html', {
        'groups': groups,
        'icons': icons,
        'favorites': favorites,
        'user_role': user_role,
    })


# View to display custom 404 page
def custom_404(request, exception):
    return render(request, '404.html', status=404)
