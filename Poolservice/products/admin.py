from django.contrib import admin

from products.models import Products
# Register your models here.

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('Code','Description', 'TC2','Price', 'Stock',)
    list_filter = ('TC2', 'Stock',)
    search_fields = ('Description',)