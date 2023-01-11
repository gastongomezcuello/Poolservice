from django.contrib import admin

from orders.models import Order
# Register your models here.

@admin.register(Order)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['client', 'product', 'quantity', 'order_date', 'payment_method', ]