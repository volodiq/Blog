from django.urls import path

from blog.feeds import LatestPostsFeed
from blog.views import PostListView, CategoryListView, PostDetailsView, SearchListView

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('category/<slug:cat_slug>', CategoryListView.as_view(), name='post_cat'),
    path('details/<slug:post_slug>', PostDetailsView.as_view(), name='post_details'),
    path('post_feed/', LatestPostsFeed(), name='post_feed'),
    path('post_search/', SearchListView.as_view(), name='post_search'),
]
