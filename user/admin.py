from django.contrib import admin

from user.models import Login


class LoginAdmin(admin.ModelAdmin):
    list_display = ["name", "username", "email", "password"]

admin.site.register(Login, LoginAdmin)