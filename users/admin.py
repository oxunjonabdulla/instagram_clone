from django.contrib import admin

from users.models import User, UserConfirmation


# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ["auth_type", "auth_status"]
    list_filter = ["auth_type", "auth_status"]
    search_fields = ['email', 'phone_number', 'username']


admin.site.register(User, UserAdmin)
admin.site.register(UserConfirmation)
