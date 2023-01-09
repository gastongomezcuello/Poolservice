from django.contrib import admin

from products.models import Products
# Register your models here.

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('Code','Description','TC2', 'Price',)
    list_filter = ('TC2',)
    search_fields = ('Description',)