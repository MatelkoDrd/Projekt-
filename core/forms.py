from django import forms


class LoginForm(forms.Form):
    username = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


class LogoutForm(forms.Form):
    pass


