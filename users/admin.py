from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role', 'phone_number', 'is_verified', 'is_active')
    list_filter = ('role', 'is_verified')
    search_fields = ('username', 'phone_number')