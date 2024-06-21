# news/models.py
from django.db import models
from django.contrib.auth.models import User  # Импортируем модель User

class News(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    short_description = models.CharField('Краткое описание', max_length=255)
    text = models.TextField('Новость')
    pub_date = models.DateTimeField('Дата публикации')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news_author')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
