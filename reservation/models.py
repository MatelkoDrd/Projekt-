from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.db.models import Q

from car.models import Car
# from user.models import User


class Reservation(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def check_dates(self):

        if Reservation.objects.\
                filter(car=self.car_id).\
                filter(
            Q(start_date__gte=self.start_date, start_date__lte=self.end_date)
           | Q(end_date__gte=self.start_date, end_date__lte=self.end_date)).\
                exists():
            print(self.start_date)
            print(self.end_date)

            return False
        if Reservation.objects.filter(car=self.car_id, start_date__lte=self.start_date, end_date__gte=self.end_date).\
            exists():
            return False

        return True