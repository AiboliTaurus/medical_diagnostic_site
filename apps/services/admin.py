from django.contrib import admin
from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_active', 'created_at')
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'description')
    list_editable = ('price', 'is_active')
    readonly_fields = ('created_at',)

    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'category', 'description', 'price')
        }),
        ('Дополнительно', {
            'fields': ('preparation', 'image', 'is_active')
        }),
        ('Системные поля', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
