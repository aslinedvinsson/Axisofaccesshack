from django import forms
from django.contrib.auth.models import User
from communication.models import Icon, Group
from .models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        # Make email, first_name, last_name explicitly required
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['role', 'about']
        widgets = {
            'role': forms.Select(attrs={'class': 'form-select'}),
            'about': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 4}
            ),
        }

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['role'].choices = UserProfile.USER_ROLES
        self.fields['about'].required = False


class IconForm(forms.ModelForm):
    class Meta:
        model = Icon
        fields = ['name', 'image', 'is_favorite', 'group']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-select'}),
        }
    
    def __init__(self, *args, prefix=None, **kwargs):
        super().__init__(*args, **kwargs)
        if prefix:
            # Update all field widget IDs to include the prefix
            for field_name, field in self.fields.items():
                field.widget.attrs['id'] = f"{prefix}_{field_name}"


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, prefix=None, **kwargs):
        super().__init__(*args, **kwargs)
        if prefix:
            for field_name, field in self.fields.items():
                field.widget.attrs['id'] = f"{prefix}_{field_name}"
