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
from django.urls import path

from email_service.views import MainView, EmailDeleteView, EmailListView, EmailDetailView, CreateEmailView, \
    EmailUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main'),  # URL-шаблон для основной страницы
    path('emails/', EmailListView.as_view(), name='email_list'),  # URL-шаблон для списка рассылок
    path('email/<int:pk>/', EmailDetailView.as_view(), name='email_detail'),  # URL-шаблон для деталей рассылки
    path('email/new/', CreateEmailView.as_view(), name='email_new'),  # URL-шаблон для создания новой рассылки
    path('email/<int:pk>/edit/', EmailUpdateView.as_view(), name='email_edit'),  # URL-шаблон для обновления рассылки
    path('email/<int:pk>/delete/', EmailDeleteView.as_view(), name='email_delete'),  # URL-шаблон для удаления рассылки
]
