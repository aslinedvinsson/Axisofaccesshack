from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserForm, UserProfileForm

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


def user_profile(request):
    return render(request, 'accounts/user_profile.html')

def caregiver_profile(request):
    return render(request, 'accounts/caregiver_profile.html')
