from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    # create a form that inherits from the UserCreationForm so we can add an email field
    email = forms.EmailField()

    class Meta:
        # gives us a nested namespace for configurations and keeps them in one place
        # when we do a form.save() it will save it to this user model
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    # don't need to add additional fields so we go straight to class Meta
    class Meta:
        model = Profile
        fields = ['image']

# these are two forms but when we put it into the template it will look like one form