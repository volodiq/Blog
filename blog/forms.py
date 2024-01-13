from django.forms import ModelForm, Textarea, TextInput, Form, CharField

from .models import Comment


class CommentForm(ModelForm):
    """ Форма создания комментария для поста """

    class Meta:
        model = Comment
        fields = ('author', 'text',)
        widgets = {
            'author': TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Имя',
                'aria-label': 'Имя пользователя',
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст комментария',
                'aria-label': 'Текст комментария',
            }),
        }


class SearchPostForm(Form):
    query = CharField()

    class Meta:
        fields = ('query',)
        widgets = {
            'query': TextInput(attrs={
                'type': 'search',
                'class': 'form-control form-control-dark',
                'placeholder': 'Поиск блога...',
                'aria-label': 'Search',
                'name': 'query'
            })
        }
