from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import UpdateView

from email_service.forms import MarketingEmailForm, BlogForm
from email_service.models import MarketingEmail, Message, Blog


# Create your views here.
class PreviewView(TemplateView):
    template_name = 'preview.html'

    @method_decorator(cache_page(60 * 15))
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class MainView(CreateView):
    template_name = 'main.html'
    model = Blog
    form_class = BlogForm
    #@method_decorator(login_required)
   #@method_decorator(cache_page(60 * 15))
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form: BlogForm):
        blog = form.save(commit=False)
        #blog.created_by = self.request.user
        blog.save()
        return reverse_lazy('main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['emails'] = MarketingEmail.objects.all()
        context['blog_posts'] = Blog.objects.all()  # добавлено
        return context

    # def post(self, request, *args, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['emails'] = MarketingEmail.objects.all()
    #     context['blog_posts'] = Blog.objects.all()  # добавлено
    #     return context


class EmailListView(ListView):
    model = MarketingEmail
    template_name = 'email_list.html'
    context_object_name = 'emails'  # Название переменной в контексте шаблона
    success_url = reverse_lazy('main')


class EmailDetailView(DetailView):
    model = MarketingEmail
    template_name = 'email_detail.html'
    context_object_name = 'email'  # Название переменной в контексте шаблона
    success_url = reverse_lazy('main')


class CreateEmailNewsletterView(CreateView):
    form_class = MarketingEmailForm
    success_url = reverse_lazy('main')
    model = MarketingEmail
    template_name = 'email_form.html'


class CreateMessageView(CreateView):
    success_url = reverse_lazy('main')
    model = Message
    template_name = 'email_new.html'
    fields = ['subject', 'body']


class EmailNewsletterUpdateView(UpdateView):
    success_url = reverse_lazy('main')
    model = MarketingEmail
    template_name = 'email_form.html'
    fields = ['email_time', 'frequency', 'clients']  # Поля, отображаемые в форме обновления


class EmailNewsletterDeleteView(DeleteView):
    success_url = reverse_lazy('main')
    model = MarketingEmail
    template_name = 'email_confirm_delete.html'
