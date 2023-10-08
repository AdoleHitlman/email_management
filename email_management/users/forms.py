from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from users.models import User
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)

class CustomAuthenticationForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ('email', 'password', 'some_data')