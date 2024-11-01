from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name', 'last_name', 'is_active', 'is_staff']
    search_fields = ['email', 'name', 'last_name']

admin.site.register(User, UserAdmin)