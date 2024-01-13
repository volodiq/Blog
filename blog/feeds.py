from django.contrib.syndication.views import Feed
from django.urls import reverse_lazy

from blog.models import Post


class LatestPostsFeed(Feed):
    title = 'Блог'
    link = reverse_lazy('blog:post_list')
    description = 'Новые посты в моем блоге'

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text[:30]

    def item_pubdate(self, item):
        return item.published_at

    def item_link(self, item):
        return reverse_lazy('blog:post_details', args=[item.slug])
