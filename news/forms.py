import datetime

from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class PostForm(forms.ModelForm):
    header = forms.CharField(max_length=128)

    class Meta:
        model = Post
        fields = [
            'type_post',
            'author',
            'header',
            'text',
            'category'
        ]

    def clean(self):
        cleaned_data = super().clean()
        header = cleaned_data.get("header")
        text = cleaned_data.get("text")
        today = datetime.datetime.now()
        last_day = today - datetime.timedelta(days=1)
        author = cleaned_data.get('author')
        posts = Post.objects.filter(time_post__gte=last_day, author=author)

        if len(posts.values_list(flat=True)) >= 3:
            raise ValidationError(
                'Один автор за сутки может публиковать не более трех постов'
            )

        if header[0].islower() or text[0].islower():
            raise ValidationError(
                "Название и текст поста должны начинаться с заглавной буквы"
            )

        if header == text:
            raise ValidationError(
                "Текст поста не может совпадать с заголовком"
            )

        return cleaned_data


