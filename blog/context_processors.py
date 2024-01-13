from blog.models import Category


def categories(request):
    """ Контекстный процессор для категорий """
    return {
        'categories': Category.objects.all()
    }
