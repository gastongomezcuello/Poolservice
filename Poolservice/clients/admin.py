from django.contrib import admin

from clients.models import Client

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
     list_display = ('client_number','name', 'kind', 'email', 'phone', 'address',)
     list_filter = ('kind',)
     search_fields = ('name', 'email', 'phone')
