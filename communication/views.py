from django.shortcuts import render
from .models import Group, Icon

def index(request):
    if request.user.is_authenticated:
        groups = Group.objects.prefetch_related('icons').all()
        for group in groups:
            group.active_icons = group.icons.filter(is_active=True)  # Add only active icons
        icons = Icon.objects.filter(is_active=True).order_by('name')  # Removed group__isnull=True
        favorites = Icon.objects.filter(is_favorite=True, is_active=True, caregiver__user=request.user).order_by('name')
    else:
        groups = None
        icons = Icon.objects.filter(is_default=True, is_active=True).order_by('name')
        favorites = None

    return render(request, 'communication/index.html', {
        'groups': groups,
        'icons': icons,
        'favorites': favorites,
    })

# View to display custom 404 page
def custom_404(request, exception):
    return render(request, '404.html', status=404)