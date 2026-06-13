from django.db import models


class Service(models.Model):
    CATEGORY_CHOICES = [
        ('mri', 'МРТ'),
        ('ct', 'КТ'),
        ('blood', 'Анализы крови'),
        ('ultrasound', 'УЗИ'),
        ('xray', 'Рентген'),
    ]

    name = models.CharField(max_length=200, verbose_name='Название')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')
    preparation = models.TextField(blank=True, verbose_name='Подготовка к исследованию')
    image = models.ImageField(upload_to='services/', blank=True, null=True, verbose_name='Изображение')
    is_active = models.BooleanField(default=True, verbose_name='Активна')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')  # <-- ДОБАВЬТЕ ЭТУ СТРОКУ

    def __str__(self):
        return f'{self.name} - {self.price} ₽'

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
