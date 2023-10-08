from django.shortcuts import render
from django.views.generic import CreateView, UpdateView

from users.forms import RegisterForm, CustomAuthenticationForm
from users.models import User


# Create your views here.
class RegisterView(CreateView):
    # Создаем обычный контроллер на создание сущности
    model = User
    form_class = RegisterForm

class UserProfileView(UpdateView):
    model = User
    form_class = CustomAuthenticationForm

    def form_valid(self, form):
        # Метод, который отрабатывает при успешной валидации формы
        if form.is_valid():
            self.object = form.save()
            # Сохранение объекта перед тем, как установить ему пароль
            if form.data.get('need_generate', False):
                self.object.set_passeword( # Функция установки пароля,
                # которая хеширует строку для того,
                # чтобы не хранить пароль в открытом виде в БД
                    self.object.make_random_password(12) # Функция генерации пароля
                )
                self.object.save()

        return super().form_valid(form)