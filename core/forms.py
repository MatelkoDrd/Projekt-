from django import forms
from django.forms import TextInput, DateInput

from reservation.models import Reservation
from user.models import User


class LoginForm(forms.Form):
    username = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


class LogoutForm(forms.Form):
    pass


class AddUserForm(forms.ModelForm):
    # first_name = forms.CharField(initial=)
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)



    # class Meta:
    #     model = Author
    #     widgets = {
    #         'name': TextInput(attrs={'placeholder': 'name'}),
    #     }


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

        password2 = cleaned_data.get("password2")
        password = cleaned_data.get("password")

        if password != password2:
            msg = "Hasła powinny być jednakowe"
            self.add_error('password2', msg)
            self.add_error('password', msg)


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['start_date', 'end_date']


