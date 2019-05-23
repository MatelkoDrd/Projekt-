from django.contrib import admin
from user.models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'password']
    list_filter = ['first_name', 'last_name', 'password']
    search_fields = ['email']


admin.site.register(User, UserAdmin)

