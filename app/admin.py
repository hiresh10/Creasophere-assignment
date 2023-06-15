from django.contrib import admin
from .models import User, UserMaster


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'city', 'location', 'project_name', 'coordinates']

@admin.register(UserMaster)
class UsermasterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone_number']