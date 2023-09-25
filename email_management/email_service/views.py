#from django.shortcuts import render
from django.views.generic import DeleteView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView
from email_service.models import MarketingEmail
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
# Create your views here.
@login_required
@cache_page(60 * 15)
class MainView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['emails'] = MarketingEmail.objects.all()
        # Дополнительная логика и данные контекста, которые вы хотите передать в шаблон
        return context

class EmailListView(ListView):
    model = MarketingEmail
    template_name = 'email_list.html'
    context_object_name = 'emails'  # Название переменной в контексте шаблона
    success_url = reverse_lazy('email_list')
class EmailDetailView(DetailView):
    model = MarketingEmail
    template_name = 'email_detail.html'
    context_object_name = 'email'  # Название переменной в контексте шаблона
    success_url = reverse_lazy('email_list')
class CreateEmailView(CreateView):
    success_url = reverse_lazy('email_list')
    model = MarketingEmail
    template_name = 'email_form.html'
    fields = ['email_time', 'frequency', 'clients']  # Поля, отображаемые в форме создания

class EmailUpdateView(UpdateView):
    success_url = reverse_lazy('email_list')
    model = MarketingEmail
    template_name = 'email_form.html'
    fields = ['email_time', 'frequency', 'clients']  # Поля, отображаемые в форме обновления

class EmailDeleteView(DeleteView):
    success_url = reverse_lazy('email_list')
    model = MarketingEmail
    template_name = 'email_confirm_delete.html'

