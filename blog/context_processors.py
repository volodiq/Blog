from blog.models import Category
from blog.forms import SearchPostForm


def categories(request):
    """ Передача всех категорий постов """
    return {
        'categories': Category.objects.all()
    }


def search_post(request):
    """ Передача формы поиска поста """
    return {
        'search_form': SearchPostForm()
    }
