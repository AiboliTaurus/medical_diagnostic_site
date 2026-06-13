from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'service', 'doctor', 'appointment_date', 'status', 'created_at')
    list_filter = ('status', 'appointment_date', 'created_at', 'service', 'doctor')
    search_fields = ('patient__username', 'patient__email', 'service__name', 'doctor__name')
    readonly_fields = ('created_at',)
    list_editable = ('status',)

    fieldsets = (
        ('Запись', {
            'fields': ('patient', 'service', 'doctor', 'appointment_date', 'status')
        }),
        ('Результаты', {
            'fields': ('result_file', 'result_summary')
        }),
        ('Дополнительно', {
            'fields': ('comment', 'created_at')
        }),
    )
