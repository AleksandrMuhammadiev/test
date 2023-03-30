from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Animal(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Информация')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='ДАта создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Животное'
        verbose_name_plural = 'Животные'

class Category(models.Model):
    cat_name = models.CharField(max_length=100, db_index=True, verbose_name='Название категории')

    def __str__(self):
        return self.cat_name


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

















