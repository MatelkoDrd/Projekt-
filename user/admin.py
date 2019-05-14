from django.contrib import admin
from user.models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
    # date_hierarchy = ['date_sent']

#
# admin.site.register(User, UserAdmin)
#
# username = models.CharField(
#
#     first_name = models.CharField(_('first name'), max_length=30, blank=True)
#     last_name = models.CharField(_('last name'), max_length=150, blank=True)
#     email = models.EmailField(_('email address'), blank=True)
#     is_staff =
#     is_active = models.BooleanField(
#
#     )
#     date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
#
#     objects = UserManager()