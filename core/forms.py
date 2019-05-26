import re

from django import forms
from django.core.exceptions import ValidationError
from django.forms import TextInput, DateInput
from reservation.models import Reservation
from user.models import User


class LoginForm(forms.Form):
    username = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


class LogoutForm(forms.Form):
    pass


def password_validator (value):

    valid_regex = "[A-z0-9]{8,}"
    if not re.match(valid_regex, value):
        raise ValidationError ("Hasło musi mieć minimum 8 znaków. W tym jedną duża literę i cyfrę")


class AddUserForm(forms.ModelForm):

    password = forms.CharField(label='Hasło',widget=forms.PasswordInput, validators=[password_validator])
    password2 = forms.CharField(label='Potwierdź', widget=forms.PasswordInput)

    class Meta:
        model = User
        widgets = {'first_name': TextInput(attrs={'placeholder': 'Janusz'}),
                   'last_name': TextInput(attrs={'placeholder': 'Kowalski'}),
                   'date_of_birth': DateInput(attrs={'placeholder': 'RRRR-MM-DD'}),
                   'email': TextInput(attrs={'placeholder': 'python@developer.pl'}),
                   'phone_number': TextInput(attrs={'placeholder': '999888777'})
                }
        fields = ['first_name', 'last_name', 'password', 'password2',
                  'date_of_birth', 'email', 'phone_number']

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password != password2:
            msg = "Hasła powinny być jednakowe"
            self.add_error('password', msg)
            self.add_error('password2', msg)


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['start_date', 'end_date']


