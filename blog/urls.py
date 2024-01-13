from django.urls import path

from blog.views import PostListView, CategoryListView

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('category/<slug:cat_slug>', CategoryListView.as_view(), name='post_cat'),
]
