from django.db import models

# Create your models here.

SEGMENT_CHOICES = (
    (1, "Basic"),
    (2, "Flex"),
    (3, "Comfort"),
    (4, "Business"),
    (5, "Luxury")
)

FUEL_CHOICES = (
    (1, "Benzyna"),
    (2, "Benzyna + LPG"),
    (3, "Diesel")

)


class Car(models.Model):
    segment = models.IntegerField(choices=SEGMENT_CHOICES)
    brand = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    fuel = models.IntegerField(choices=FUEL_CHOICES)


class User(models.Model):
    first_name = models.CharField(max_length=32)
    second_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(max_length=128)
    year_of_birth = models.IntegerField()
    card_number = models.BigIntegerField()
