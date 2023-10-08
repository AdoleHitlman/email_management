from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from users.models import User
class RegisterForm(UserCreationForm):
    # Наследуемся от специальной формы UserCreationForm из модуля auth
    class Meta:
        model = User
        # Указываем новую кастомную модель
        fields = ('email', 'password1', 'password2',)

class CustomAuthenticationForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ('email', 'password', 'some_data')