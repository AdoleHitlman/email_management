from django import forms
from .models import MarketingEmail
from datetime import datetime
from .models import Blog
from users.models import User
from django.urls import reverse

class MarketingEmailForm(forms.ModelForm):
    email_date = forms.DateField(
        label='Дата отправки',
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
    )
    email_time = forms.TimeField(
        label='Время отправки',
        input_formats=['%H:%M'],
        widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
    )
    clients = forms.ModelMultipleChoiceField(queryset=User.objects.all())

    class Meta:
        model = MarketingEmail
        fields = ['email_date', 'email_time', 'frequency','clients', 'message']

    def save(self, commit=True):
        instance = super().save(commit=False)
        email_date = self.cleaned_data['email_date']
        email_time = self.cleaned_data['email_time']
        instance.email_time = datetime.combine(email_date, email_time)
        if commit:
            instance.save()
        return instance

class MessageForm(forms.ModelForm):
    class Meta:
        fields = ['subject', 'body']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'preview']

