from sso.models import Clients
from django.contrib import admin

class ClientsAdmin(admin.ModelAdmin):
    fields = ['name', 'url']
    
admin.site.register(Clients,ClientsAdmin)
