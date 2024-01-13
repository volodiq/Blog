from django.utils import timezone
from django.db import models


class PublishedManager(models.Manager):
    """ Модельный менеджер для опубликованных постов """

    def get_queryset(self):
        """ Получение постов со статусом опубликовано """
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    """ Посты блога """

    class Meta:
        indexes = [models.Index(fields=['category', '-published_at'])]
        ordering = ('-published_at',)
        verbose_name_plural = 'Посты'

    class Status(models.TextChoices):
        """ Статус поста """
        DRAFT = 'DR', 'Черновик'
        PUBLISHED = 'PB', 'Опубликовано'

    # Модельные менеджеры
    objects = models.Manager()
    published = PublishedManager()

    text = models.TextField('Содержание поста')
    title = models.CharField('Заголовок поста', max_length=200)
    slug = models.SlugField('Slug поста', max_length=200, unique=True)
    published_at = models.DateTimeField('Дата публикации поста', default=timezone.now)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='author')
    category = models.ForeignKey('blog.Category', on_delete=models.CASCADE, related_name='category')
    status = models.CharField('Статус поста', max_length=2, choices=Status.choices, default=Status.DRAFT)

    def __str__(self):
        return self.title


class Category(models.Model):
    """ Категории постов """

    class Meta:
        verbose_name_plural = 'Категории'

    name = models.CharField('Название категории постов', max_length=200)
    slug = models.SlugField('Slug категории постов', max_length=200, unique=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    """ Комментарии поста """

    class Meta:
        indexes = [models.Index(fields=['published_at'])]
        ordering = ['-published_at']
        verbose_name = 'Комментарии'

    text = models.TextField()
    author = models.CharField(max_length=30)
    published_at = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comment')

    def __str__(self):
        return f'{self.author} | {self.post}'
