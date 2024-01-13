from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy

from blog.forms import CommentForm
from blog.models import Post, Comment


class PostListView(ListView):
    """ Список всех опубликованных постов """
    queryset = Post.published.all()
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 3


class CategoryListView(ListView):
    """ Список всех опубликованных постов в категории n """
    extra_context = {'is_category': True}
    template_name = 'post_list.html'
    context_object_name = 'posts'
    slug_url_kwarg = 'cat_slug'
    paginate_by = 3
    model = Post


class PostDetailsView(FormMixin, DetailView):
    """ Подробности поста """
    template_name = 'post_details.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'
    model = Post
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('blog:post_details', args=(self.kwargs['post_slug'],))

    def get_context_data(self, **kwargs):
        context = super(PostDetailsView, self).get_context_data(**kwargs)
        post = Post.published.get(slug=self.kwargs['post_slug'])
        context['comments'] = Comment.objects.filter(post=post)
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        post = Post.published.get(slug=self.kwargs['post_slug'])
        form.instance.post = post
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(PostDetailsView, self).form_valid(form)
