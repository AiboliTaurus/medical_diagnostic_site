from django.db import models
from django.conf import settings
from apps.services.models import Service
from apps.pages.models import Doctor  # Добавьте этот импорт


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидает'),
        ('confirmed', 'Подтверждён'),
        ('completed', 'Завершён'),
        ('cancelled', 'Отменён'),
    ]

    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='appointments',
                                verbose_name='Пациент')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Услуга')
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True,
                               verbose_name='Врач')  # Добавьте это поле
    appointment_date = models.DateTimeField(verbose_name='Дата и время приёма')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='Статус')
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    result_file = models.FileField(upload_to='results/', blank=True, null=True, verbose_name='Результат диагностики')
    result_summary = models.TextField(blank=True, verbose_name='Заключение')

    def __str__(self):
        return f'{self.patient} - {self.service} - {self.appointment_date}'

    class Meta:
        verbose_name = 'Запись на приём'
        verbose_name_plural = 'Записи на приём'
        ordering = ['-appointment_date']
