from django.contrib import admin
from car.models import Car
# Register your models here.


class CarAdmin(admin.ModelAdmin):
    list_display = ['segment', 'brand', 'model', 'fuel']
    list_filter = ['segment', 'brand', 'model', 'fuel']
    search_fields = ['segment', 'brand', 'model']


admin.site.register(Car, CarAdmin)


