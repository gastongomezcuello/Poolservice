from django.contrib import admin

from clients.models import Clients

# Register your models here.
@admin.register(Clients)
class ClientAdmin(admin.ModelAdmin):
     list_display = ('name', 'kind', 'email', 'phone', 'address',)
     list_filter = ('kind',)
     search_fields = ('name', 'email', 'phone')
