from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_title', 'service_genre', 'service_des')
    search_fields = ('service_title', 'service_genre')

admin.site.register(Service, ServiceAdmin)
