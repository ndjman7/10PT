from django import forms
from django.contrib.auth import get_user_model

__all__ = [
    'SignInModelForm',
]


class SignInModelForm(forms.ModelForm):

    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = get_user_model()
        fields = [
            'email',
            'password',
        ]
