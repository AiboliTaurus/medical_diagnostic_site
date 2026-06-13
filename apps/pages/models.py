from django.db import models
from apps.services.models import Service


class CompanyInfo(models.Model):
    history = models.TextField(verbose_name='История компании', blank=True)
    mission = models.TextField(verbose_name='Миссия и ценности', blank=True)
    address = models.CharField(max_length=300, verbose_name='Адрес', blank=True)
    phone = models.CharField(max_length=20, verbose_name='Телефон', blank=True)
    email = models.EmailField(verbose_name='Email', blank=True)

    def __str__(self):
        return 'Информация о компании'

    class Meta:
        verbose_name = 'Информация о компании'
        verbose_name_plural = 'Информация о компании'


class Doctor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя врача')
    specialty = models.CharField(max_length=100, verbose_name='Специализация')
    bio = models.TextField(verbose_name='Биография', blank=True)
    photo = models.ImageField(upload_to='doctors/', blank=True, null=True, verbose_name='Фото')
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок вывода')
    services = models.ManyToManyField(Service, blank=True, verbose_name='Услуги',
                                      help_text='Услуги, которые может проводить этот врач')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'
        ordering = ['order', 'name']
