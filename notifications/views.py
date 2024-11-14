from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Notification

def index(request):
    notifications = Notification.objects.all()
    return render(request, 'notificationindex.html', {'notifications': notifications})


