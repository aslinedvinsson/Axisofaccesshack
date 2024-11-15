from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserForm, UserProfileForm
from .models import UserProfile
from communication.models import Icon

def register(request):
    """
    Handles the creation of a new user and their profile in :model:`accounts.User` and :model:`accounts.UserProfile`.

    **Arguments:**

    ``request``
    The HTTP request.

    **POST:**

    User information is validated and if valid, a new User is created along with their profile.
    After creation, the user is redirected to the home page.

    **GET:**

    An empty registration form for User and UserProfile is displayed.

    **Template:**

    :template:`accounts/register.html`
    """
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)  # Don't save the User instance yet
            user.set_password(user_form.cleaned_data['password'])  # Set the password
            user.save()  # Now save the User instance
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            # Specify the allauth backend
            user.backend = 'allauth.account.auth_backends.AuthenticationBackend'
            login(request, user)  # Log in the user
            messages.add_message(request, messages.SUCCESS, 'Congratulations, you have successfully registered!')
            return redirect('index')
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'accounts/register.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def user_profile(request):
    """
    Displays the profile page for a user (either regular or caregiver),
    including assigned end users and icon management options for caregivers.
    """
    user_profile = request.user.userprofile  # Get the current logged-in user's profile

    # For caregivers (role == 'CG'), show icons and assigned end users
    if user_profile.role == 'CG':
        caregiver_icons = Icon.objects.filter(caregiver=user_profile)  # Get the caregiver's icons
        assigned_end_users = user_profile.end_users.all()  # Get the end users assigned to this caregiver
    else:
        caregiver_icons = []  # No icons for regular users
        assigned_end_users = []  # No assigned end users for regular users

    # Render the appropriate template based on the role of the user
    if user_profile.role == 'CG':
        return render(request, 'accounts/caregiver_profile.html', {
            'user_profile': user_profile,
            'caregiver_icons': caregiver_icons,
            'assigned_end_users': assigned_end_users,
        })
    else:
        return render(request, 'accounts/user_profile.html', {
            'user_profile': user_profile,
        })


@login_required
def add_or_edit_icon(request):
    """
    Adds a new icon or edits an existing icon for the caregiver.
    """
    if request.method == 'POST':
        icon_name = request.POST.get('icon_name')
        icon_id = request.POST.get('icon_id')

        user_profile = request.user.userprofile

        if icon_id:
            # Edit existing icon
            icon = Icon.objects.get(id=icon_id)
            icon.name = icon_name
            icon.save()
        else:
            # Add new icon
            Icon.objects.create(caregiver=user_profile, name=icon_name)

        return redirect('caregiver_profile')


@login_required
def delete_icon(request, icon_id):
    """
    Deletes a specified icon for the caregiver.
    """
    if request.method == 'POST':
        try:
            icon = Icon.objects.get(id=icon_id)
            icon.delete()
            return JsonResponse({'success': True})
        except Icon.DoesNotExist:
            return JsonResponse({'success': False}, status=404)

    return JsonResponse({'success': False}, status=400)