from django.urls import path
from . import views


urlpatterns = [
    path('', views.register, name='register'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('manage_end_users/', views.manage_end_users, name='manage_end_users'),
    path(
      'toggle_favorite/<int:icon_id>/',
      views.toggle_favorite,
      name='toggle_favorite'
    ),

    # Icon Management
    path('add_icon/', views.add_icon, name='add_icon'),
    path('edit_icon/<int:icon_id>/', views.edit_icon, name='edit_icon'),
    path('delete_icon/<int:icon_id>/', views.delete_icon, name='delete_icon'),

    # Group Management
    path('add_group/', views.add_group, name='add_group'),
    path('edit_group/<int:group_id>/', views.edit_group, name='edit_group'),
    path(
      'delete_group/<int:group_id>/',
      views.delete_group,
      name='delete_group'
    ),
]
