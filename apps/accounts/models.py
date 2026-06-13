from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=20, unique=True, verbose_name='Телефон')
    is_patient = models.BooleanField(default=True, verbose_name='Пациент')
    is_doctor = models.BooleanField(default=False, verbose_name='Врач')

    def __str__(self):
        return f'{self.get_full_name()} ({self.username})'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
