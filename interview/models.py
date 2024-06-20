from django.db import models
import uuid


class Offer(models.Model):
    STATUS_CHOICES = (
        (1, 'На рассмотрении'),
        (2, 'Прошел собеседование'),
        (3, 'Получил оффер'),
        (4, 'Отказ'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=150, null=False, blank=False, verbose_name='Заголовок')
    link = models.URLField(null=False, blank=True, verbose_name='Ссылка')
    description = models.TextField(null=False, blank=True, verbose_name='Описание')

    salary = models.CharField(max_length=100, null=True, blank=True, verbose_name='Оклад')
    location = models.CharField(max_length=150, null=True, blank=True, verbose_name='Город')
    employment_type = models.CharField(max_length=100, choices=(('remote', 'Удаленная работа'), ('office', 'Офис')),
                                       default='remote', verbose_name='Тип занятости')
    publish_date = models.DateTimeField(null=True, blank=True, verbose_name='Дата публикации')
    contact_info = models.CharField(max_length=200, null=True, blank=True, verbose_name='Контактная информация')
    comments = models.TextField(blank=True, verbose_name='Комменатрий')
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, verbose_name='Статус')

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
