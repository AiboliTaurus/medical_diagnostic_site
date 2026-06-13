from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('create/', views.appointment_create, name='appointment_create'),
    path('create/<int:service_id>/', views.appointment_create, name='appointment_create_with_service'),
    path('cancel/<int:pk>/', views.appointment_cancel, name='appointment_cancel'),
]
