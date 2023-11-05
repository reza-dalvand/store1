from django.contrib import admin

from accounts_module.models import CustomUser

# Register your models here.
admin.site.register(CustomUser)