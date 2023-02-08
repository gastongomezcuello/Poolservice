from django.contrib import admin

from clients.models import Client

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
     list_display = ('id', 'kind', 'phone', 'address',)
     list_filter = ('kind',)
     search_fields = ('phone',)
