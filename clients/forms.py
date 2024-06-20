from django import forms
from clients.models import Client


class ClientStatusForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['status']
