from django import forms
from django.urls import reverse

from .models import MarketingEmail


class MarketingEmailForm(forms.ModelForm):
    class Meta:
        model = MarketingEmail
        fields = ['email_time', 'frequency', 'status', 'clients']
