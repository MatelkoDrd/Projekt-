from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from django.template.response import TemplateResponse
from django.views import View

from core.forms import LoginForm, LogoutForm


class BaseView(View):

    def get(self, request):
#         html = """
# """
#         class_list = []
#         for school_class in SCHOOL_CLASS:
#             class_list.append("<li><a href='/class/{}'>{}</a></li>".format(school_class[0], school_class[1]))
#         classes_part = "".join(class_list)
#         return HttpResponse(html.format(classes_part))
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