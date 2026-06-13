from django.contrib import admin
from .models import CompanyInfo, Doctor


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'phone', 'email')

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return True


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'order', 'id')
    list_editable = ('order',)
    search_fields = ('name', 'specialty')
    list_filter = ('specialty', 'services')

    filter_horizontal = ('services',)

    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'specialty', 'bio')
        }),
        ('Услуги', {
            'fields': ('services',)
        }),
        ('Медиа', {
            'fields': ('photo',)
        }),
        ('Сортировка', {
            'fields': ('order',)
        }),
    )
