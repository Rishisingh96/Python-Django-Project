from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_title', 'service_genre', 'service_des', 'get_image_preview')
    search_fields = ('service_title', 'service_genre')
    list_filter = ('service_genre',)
    
    def get_image_preview(self, obj):
        if obj.service_icon:
            return f'<img src="{obj.service_icon.url}" width="50" height="50" style="object-fit: cover;" />'
        return "No Image"
    get_image_preview.short_description = 'Image Preview'
    get_image_preview.allow_tags = True

admin.site.register(Service, ServiceAdmin)
