# forms.py
from django.contrib.auth.forms import AuthenticationForm
from django.forms import TextInput

from .models import User


class UserAuthenticationForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'username'
                }),
            'password': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'password'
                })
        }

