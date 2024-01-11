from django.shortcuts import render
from django.views.generic import ListView

from blog.models import Post


class PostListView(ListView):
    """ Список всех опубликованных постов """
    queryset = Post.published.all()
    context_object_name = 'posts'
    template_name = 'post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_is_author'] = self.request.user.is_superuser
        return context
