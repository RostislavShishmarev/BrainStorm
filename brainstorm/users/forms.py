import re

import django.forms
import django.contrib.auth.forms

import core.forms
import users.models


class CustomUserCreationForm(
    core.forms.BootstrapFormMixin, django.contrib.auth.forms.UserCreationForm
):
    class Meta:
        model = users.models.User
        fields = (
            users.models.User.username.field.name,
            users.models.User.email.field.name,
            'password1',
            'password2',
        )

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.match(r'^[\w-]+$', username):
            raise django.forms.ValidationError('Недопустимое имя пользователя')
        return username


class UserProfileForm(core.forms.BootstrapFormMixin, django.forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[users.models.User.bio.field.name].required = False

    class Meta:
        model = users.models.User
        fields = [
            users.models.User.email.field.name,
            users.models.User.username.field.name,
            users.models.User.first_name.field.name,
            users.models.User.last_name.field.name,
            users.models.User.bio.field.name,
            users.models.User.image.field.name,
        ]


class LoginForm(
    core.forms.BootstrapFormMixin,
    django.contrib.auth.forms.AuthenticationForm,
):
    pass


class PasswordChangeForm(
    core.forms.BootstrapFormMixin,
    django.contrib.auth.forms.PasswordChangeForm,
):
    pass


class PasswordResetForm(
    core.forms.BootstrapFormMixin,
    django.contrib.auth.forms.PasswordResetForm,
):
    pass
