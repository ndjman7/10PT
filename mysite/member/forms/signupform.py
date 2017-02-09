from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth import get_user_model
from ..models import UserInfo

__all__ = [
    'SignUpModelForm',
]


class SignUpModelForm(forms.ModelForm):

    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField()

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
