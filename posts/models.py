# from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Post(models.Model):

    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор записи',
    )

    title = models.CharField(
        max_length=50,
        verbose_name='Заголовок поста',
    )

    text = models.TextField(
        blank=False,
        null=False,
        verbose_name='Текст статьи'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления',
    )

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:posts')
