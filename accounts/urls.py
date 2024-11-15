from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('add_or_edit_icon/', views.add_or_edit_icon, name='add_or_edit_icon'),
    path('delete-icon/<int:icon_id>/', views.delete_icon, name='delete_icon'),
]