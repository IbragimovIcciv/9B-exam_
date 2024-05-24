from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import Users, conatact_us


class SignupForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ContactForm(ModelForm):
    class Meta:
        model = conatact_us
        fields = '__all__'