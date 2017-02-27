from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth import get_user_model
from ..models import UserInfo

__all__ = [
    'SignUpModelForm',
]


class SignUpModelForm(forms.ModelForm):

    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
    }

    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your email address',
        }))
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Pick a username',
        }))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Create a password',
        }))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Confirm a password',
        }))

    class Meta:
        model = get_user_model()
        fields = [
            'email',
            'username',
            'password1',
            'password2',
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        password_validation.validate_password(
            self.cleaned_data['password2'],
            self.instance
        )
        return password2

    def save(self, commit=True):
        user = super(SignUpModelForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.save()
        UserInfo.objects.create(user=user, username=self.cleaned_data.get('username'))
        return user
