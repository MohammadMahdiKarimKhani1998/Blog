from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email',)


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder': 'Password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder': 'Password confirmation'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    # first_name = forms.CharField(label=_('first_name'))
    # last_name = forms.CharField(label=_('last_name'))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'mobile']
        widgets = {'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
                   'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile'}), }


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}),
        label='Email')
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}),
        label='Password')

    class Meta:
        fields = ['email', 'password']
