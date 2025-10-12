from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import (
    User,
    Shop,
    Category,
    Product,
    Contact,
    Order,
    OrderItem,
    ConfirmEmailToken,
)

# Регистрация моделей в админке
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'type', 'is_active')
    list_filter = ('type', 'is_active')
    search_fields = ('email', 'company', 'position')
    ordering = ('email',)

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'shop', 'price', 'quantity')
    list_filter = ('shop',)
    search_fields = ('name', 'model')
    ordering = ('-name',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'city', 'street', 'phone')
    search_fields = ('city', 'street', 'phone')
    list_filter = ('city',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'dt', 'state')
    list_filter = ('state',)
    search_fields = ('user__email',)
    ordering = ('-dt',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product_info', 'quantity')
    search_fields = ('order__id', 'product_info__name')
    list_filter = ('order__state',)

@admin.register(ConfirmEmailToken)
class ConfirmEmailTokenAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'key')
    search_fields = ('user__email', 'key')