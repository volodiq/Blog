from django.utils import timezone
from django.db import models


class Post(models.Model):
    """ Посты блога """

    class Status(models.TextChoices):
        """ Статус поста """
        DRAFT = 'DR', 'Черновик'
        PUBLISHED = 'PB', 'Опубликовано'

    text = models.TextField('Содержание поста')
    title = models.CharField('Заголовок поста', max_length=200)
    slug = models.SlugField('Slug поста', max_length=200, unique=True)
    published_at = models.DateTimeField('Дата публикации поста', default=timezone.now)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='author')
    category = models.ForeignKey('blog.Category', on_delete=models.CASCADE, related_name='category')
    status = models.CharField('Статус поста', max_length=2, choices=Status.choices, default=Status.DRAFT)


class Category(models.Model):
    """ Категории постов """
    name = models.CharField('Название категории постов', max_length=200)
    slug = models.SlugField('Slug категории постов', max_length=200, unique=True)