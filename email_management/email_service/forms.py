from django.urls import reverse
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

from .models import MarketingEmail


class MarketingEmailForm(forms.ModelForm):
    class Meta:
        model = MarketingEmail
        fields = ['email_time', 'frequency', 'status', 'clients']
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]