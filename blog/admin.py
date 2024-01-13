from django.contrib import admin

from .models import Category, Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'published_at']
    search_fields = ['title', 'text']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-published_at']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Comment)
