from django.views.generic import ListView

from blog.models import Post, Category


class PostListView(ListView):
    """ Список всех опубликованных постов """
    queryset = Post.published.all()
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 3


class CategoryListView(ListView):
    """ Список всех опубликованных постов в категории n """
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 3
    extra_context = {'is_category': True}

    def get_queryset(self):
        """ Получение постов в категории """
        return Post.published.filter(category__slug=self.kwargs.get('cat_slug'))
