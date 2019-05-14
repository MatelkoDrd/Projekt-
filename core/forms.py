from django import forms

from user.models import User


class LoginForm(forms.Form):
    username = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


class LogoutForm(forms.Form):
    pass


class AddUserForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
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
