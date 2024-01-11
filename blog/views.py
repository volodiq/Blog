from django.shortcuts import render


def index(request):
    user_is_author = request.user.is_superuser
    return render(request, 'base.html', context={'user_is_author': user_is_author})
