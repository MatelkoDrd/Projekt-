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
    quantity = models.IntegerField()

    def __str__(self):
        return self.model

