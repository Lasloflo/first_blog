from django.db import models

# Create your models here.
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок статьи')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Имя автора')
    content = models.TextField(null=True, blank=True, verbose_name='Статья')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    is_active = models.BooleanField(default=True, db_index=True, verbose_name='Опубликовать?')
    image = models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/', verbose_name='Изображение')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-published']

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, verbose_name='Статья')
    author = models.CharField(max_length=30, verbose_name='Автор')
    content = models.TextField(verbose_name='Содержание')
    is_active = models.BooleanField(default=True, db_index=True, verbose_name='Выводить на экран?')
    create_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликован')

    class Meta:
        verbose_name_plural = "Комментарии"
        verbose_name = "Комментарий"
        ordering = ['create_at']
