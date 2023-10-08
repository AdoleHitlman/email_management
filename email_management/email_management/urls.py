"""
URL configuration for email_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from django.contrib import auth
from users.views import RegisterView
from email_service.views import MainView, EmailNewsletterDeleteView, EmailListView, EmailDetailView, CreateEmailNewsletterView, \
    EmailNewsletterUpdateView,CreateMessageView,PreviewView

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/',RegisterView.as_view(),name='register'),
    path('admin/', admin.site.urls),
    path('', PreviewView.as_view(), name='preview'),
    path('main', MainView.as_view(), name='main'),  # URL-шаблон для основной страницы
    path('emails/', EmailListView.as_view(), name='email_list'),  # URL-шаблон для списка рассылок
    path('email/<int:pk>/', EmailDetailView.as_view(), name='email_detail'),  # URL-шаблон для деталей рассылки
    path('email/new/newsletter', CreateEmailNewsletterView.as_view(), name='email_new_newsletter'),# URL-шаблон для создания новой рассылки
    path('email/new/message',CreateMessageView.as_view(),name='email_new_message'),
    path('email/<int:pk>/edit/', EmailNewsletterUpdateView.as_view(), name='email_edit'),  # URL-шаблон для обновления рассылки
    path('email/<int:pk>/delete/', EmailNewsletterDeleteView.as_view(), name='email_delete'),  # URL-шаблон для удаления рассылки
]
