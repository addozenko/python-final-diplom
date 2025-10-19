from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import (
    User,
)

# Регистрация моделей в админке
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'type', 'is_active')
    list_filter = ('type', 'is_active')
    search_fields = ('email', 'company', 'position')
    ordering = ('email',)