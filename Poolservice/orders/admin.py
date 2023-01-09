from django.contrib import admin

from orders.models import Orders
# Register your models here.

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['client', 'product', 'quantity', 'order_date', 'payment_method', ]