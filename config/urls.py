from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.pages.views import get_doctors_by_service  # Добавьте этот импорт

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.pages.urls')),
    path('services/', include('apps.services.urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('appointments/', include('apps.appointments.urls')),
    path('api/get_doctors_by_service/', get_doctors_by_service, name='get_doctors_by_service'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
