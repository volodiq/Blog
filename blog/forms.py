from django.forms import ModelForm, Textarea, TextInput

from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)
        widgets = {
            'author': TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Имя',
                'aria-label': 'Имя пользователя'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст комментария',
                'aria-label': 'Текст комментария'
            }),
        }
