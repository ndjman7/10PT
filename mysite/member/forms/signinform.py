from django import forms
from django.contrib.auth import get_user_model

__all__ = [
    'SignInModelForm',
]


class SignInModelForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = [
            'email',
            'password',
        ]
