from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/register/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('communication.urls')),
    path('notifications/', include('notifications.urls')), 
]

handler404 = 'communication.views.custom_404'
