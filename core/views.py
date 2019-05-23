from datetime import date, timedelta
from smsapi.client import SmsApiPlClient
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.http import HttpResponse, request
from django.shortcuts import render, redirect

# Create your views here.
from django.template.response import TemplateResponse
from django.views import View

from car.models import SEGMENT_CHOICES, Car
from core.forms import LoginForm, LogoutForm, AddUserForm, ReservationForm
from core.functions import calculate_price
from reservation.models import Reservation
from user.models import User

from  django.core.mail import send_mail
from django.conf import settings





class BaseView(View):
    def get(self, request):
        return TemplateResponse(request, 'segments_base.html', {'segments': SEGMENT_CHOICES})


class SegmentView(View):
    def get(self, request, segment):
        cars = Car.objects.filter(segment=segment)
        return render(request, 'segments.html', {'cars': cars})


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
                return render(request, 'login.html', {'form': form, 'message': 'Nie ma takiego uzytkownika'})
        else:
            return render(request, 'login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        form = LogoutForm
        return render(request, 'logout.html', {'form': form, 'message': 'Zostałeś wylogowany'})

    def post(self,request):
        logout(request)
        return redirect('/login')


class AddUserView(View):
    def get(self, request):
        form = AddUserForm()
        return render(request, 'add_user.html', {'form': form})

    def post(self, request):
        form = AddUserForm(request.POST)
        if form.is_valid():
            del form.cleaned_data['password2']
            new_user = User.objects.create_user(**form.cleaned_data)
            return redirect ('/')
        else:
            return render(request, 'add_user.html', {'form': form})


class CarView(LoginRequiredMixin, View):
    login_url = '/login'

    def get(self, request, car):
        description = Car.objects.get(id=car)
        form = ReservationForm()
        return render(request, 'car_view.html', {'description': description, 'form': form})

    def post(self, request, car):
        form = ReservationForm(request.POST)
        description = Car.objects.get(id=car)
        if not request.user.is_authenticated:
            return redirect('/login')

        if form.is_valid():
            data1 = form.cleaned_data['start_date']
            data2 = form.cleaned_data['end_date']
            reservation = Reservation(user=request.user, car=description,
                                                     start_date=data1, end_date=data2)
            is_available = reservation.check_dates()

            if data1 > data2:
                return render(request, 'car_view.html', {'description': description, 'form': form,
                                                         'message': 'Data zakończenia wynajmu jest wcześniejsza niż rozpoczęcia!'})

            if is_available:
                reservation.save()
                return redirect('/email')
            else:
                return render(request, 'car_view.html', {'description': description, 'form': form,
                                                         'message': 'Auto jest niedostępne w tym terminie!'})

        else:
            return render(request, 'car_view.html', {'description': description, 'form': form})


def load_dates(request):
    print(request.GET)

    start_date_id = request.GET.get('start_date')
    end_date_id = request.GET.get('end_date')
    segment = int(request.GET.get('segment'))
    date_form = ReservationForm(request.GET)
    if date_form.is_valid():
        start_date = date_form.cleaned_data['start_date']
        end_date = date_form.cleaned_data['end_date']
        price = calculate_price(segment, end_date, start_date, 100)
        return HttpResponse(str(price))
    return HttpResponse('')


class SuccessView(View):
    def get(self, request):
        return render(request, 'success.html', {})


def email(request):

    client = SmsApiPlClient(access_token='sTwdrplwMHB72lX8HJaGROVJubT5jyK2bCOalalK')

    phone_number = request.user.phone_number
    print('phone number', phone_number)
    r = client.sms.send(to=phone_number,
                        message='Sprawdź maila :)')

    email_address = (request.user.email,)
    subject = "Dziękujemy za wypożyczenie naszego samochodu 1!11!!!"
    message = 'Zapraszamy na Pizzowy Piatek z Pythonem do CodersLab :)'
    email_from = settings.EMAIL_HOST_USER


    send_mail(subject, message, email_from, email_address)

    return redirect('/success')

