from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})


class SignUpForm(UserCreationForm):
    class Meta:
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name']
        model = User

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})
