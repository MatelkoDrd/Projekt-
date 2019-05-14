from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template.response import TemplateResponse
from django.views import View

from core.forms import LoginForm, LogoutForm, AddUserForm
from user.models import User


class BaseView(View):

    def get(self, request):
        return TemplateResponse(request, 'base.html', {})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        next_page = request.GET.get('next')
        print(next_page)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                if next_page:
                    return redirect(next_page)
                return redirect('/')
            else:
                return render(request, 'login.html', {'form': form, 'message': 'NIe ma takiego uzytkownika'})
        else:
            return render(request, 'login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        form = LogoutForm
        return render(request, 'logout.html', {'form': form, 'message': 'Zostałeś wylogowany'})

    def post(self,request):
        return redirect('/')


class AddUserView(View):
    def get(self, request):
        form = AddUserForm()
        return render(request, 'add_user.html', {'form': form})

    def post(self, request):
        form = AddUserForm(request.POST)
        if form.is_valid():
            del form.cleaned_data['password2']
            new_user = User.objects.create_user(**form.cleaned_data)
            return HttpResponse("Witaj: {}".format(new_user.first_name))
        else:
            return render(request, 'add_user.html', {'form': form})