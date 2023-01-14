from django.contrib import admin

from products.models import Product
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('code','description', 'tc','price', 'stock',)
    list_filter = ('tc', 'stock',)
    search_fields = ('description',)