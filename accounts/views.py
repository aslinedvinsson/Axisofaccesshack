from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from communication.models import Icon, Group
from .forms import UserForm, UserProfileForm, IconForm, GroupForm
from .models import UserProfile

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
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            # Set the email and name fields from the user instance
            profile.email = user.email
            profile.name = f"{user.first_name} {user.last_name}"
            profile.save()

            user.backend = 'allauth.account.auth_backends.AuthenticationBackend'
            login(request, user)
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

    if user_profile.role == 'CG':
        caregiver_icons = Icon.objects.filter(caregiver=user_profile)  # Get the caregiver's icons
        caregiver_groups = Group.objects.filter(caregiver=user_profile)  # Get the caregiver's groups
        assigned_end_users = user_profile.end_users.all()  # Get the end users assigned to this caregiver

        # Attach a form to each icon and group
        for icon in caregiver_icons:
            icon.form = IconForm(instance=icon)

        for group in caregiver_groups:
            group.form = GroupForm(instance=group)

        # Instantiate forms for adding new icons/groups (empty forms)
        icon_form = IconForm()
        group_form = GroupForm()

        # Render the caregiver profile template with the forms included
        return render(request, 'accounts/caregiver_profile.html', {
            'user_profile': user_profile,
            'caregiver_icons': caregiver_icons,
            'caregiver_groups': caregiver_groups,
            'assigned_end_users': assigned_end_users,
            'icon_form': icon_form,  # For adding new icons
            'group_form': group_form,  # For adding new groups
        })

    else:
        return render(request, 'accounts/user_profile.html', {
            'user_profile': user_profile,
        })


@login_required
def toggle_favorite(request, icon_id):
    """
    Toggles the favorite status of an icon.
    """
    try:
        icon = Icon.objects.get(id=icon_id, caregiver=request.user.userprofile)
        icon.is_favorite = not icon.is_favorite
        icon.save()
        return redirect('user_profile')
    except Icon.DoesNotExist:
        return redirect('user_profile')


# Adding a new icon
@login_required
def add_icon(request):
    if request.method == 'POST':
        form = IconForm(request.POST, request.FILES)
        if form.is_valid():
            icon = form.save(commit=False)
            icon.caregiver = request.user.userprofile
            icon.save()
            return redirect('user_profile')
    else:
        form = IconForm()
    return render(request, 'accounts/caregiver_profile.html', {'icon_form': form})


# Editing an existing icon
@login_required
def edit_icon(request, icon_id):
    icon = get_object_or_404(Icon, id=icon_id, caregiver=request.user.userprofile)
    if request.method == 'POST':
        form = IconForm(request.POST, request.FILES, instance=icon)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = IconForm(instance=icon)
    return render(request, 'accounts/caregiver_profile.html', {'icon_form': form})


# Adding a new group
@login_required
def add_group(request):
    """
    Allows a caregiver to add a new group, automatically associating it with their profile.
    """
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.caregiver = request.user.userprofile  # Assign the logged-in user as the caregiver
            group.save()
            return redirect('user_profile')
    else:
        form = GroupForm()
    
    return render(request, 'accounts/caregiver_profile.html', {'group_form': form})


# Editing an existing group
@login_required
def edit_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = GroupForm(instance=group)
    return render(request, 'accounts/caregiver_profile.html', {'group_form': form})

# Deleting an icon
@login_required
def delete_icon(request, icon_id):
    """
    Deletes a specific icon.
    """
    if request.method == 'POST':
        try:
            icon = Icon.objects.get(id=icon_id, caregiver=request.user.userprofile)
            icon.delete()
            return redirect('user_profile')
        except Icon.DoesNotExist:
            return redirect('user_profile')

#Editing a group
@login_required
def delete_group(request, group_id):
    """
    Deletes a specific group.
    """
    if request.method == 'POST':
        try:
            group = Group.objects.get(id=group_id)
            group.delete()
            return redirect('user_profile')
        except Group.DoesNotExist:
            return redirect('user_profile')