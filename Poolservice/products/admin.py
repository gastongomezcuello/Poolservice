from django.contrib import admin

from products.models import Products
# Register your models here.

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('code','description','tc2', 'price', 'stock')
    list_filter = ('stock',)
    search_fields = ('description',)