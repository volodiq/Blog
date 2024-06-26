# Generated by Django 5.0.1 on 2024-01-10 14:30

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название категории постов')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='Slug категории постов')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Содержание поста')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок поста')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='Slug поста')),
                ('published_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации поста')),
                ('status', models.CharField(choices=[('DR', 'Черновик'), ('PB', 'Опубликовано')], default='DR', max_length=2, verbose_name='Статус поста')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='blog.category')),
            ],
        ),
    ]
