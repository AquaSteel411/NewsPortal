from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.cache import cache


class Author(models.Model):
    rating_user = models.IntegerField(default=0)

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def update_rating(self):
        post_rating = sum(Post.objects.filter(author=self).values_list('rating_news', flat=True)) * 3
        com_rating = sum(Comment.objects.filter(user__author=self).values_list('rating_com', flat=True))
        com_post_rating = sum(Comment.objects.filter(post__in=Post.objects.filter(author=self)).
                              values_list('rating_com', flat=True))
        self.rating_user = post_rating + com_rating + com_post_rating
        self.save()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    topic = models.CharField(max_length=64, unique=True)
    subscribers = models.ManyToManyField(User, related_name='categories')

    def __str__(self):
        return self.topic


class Post(models.Model):
    article = 'AR'
    news = 'NW'

    TYPES = [
        (article, 'Статья'),
        (news, 'Новость')
    ]

    time_post = models.DateTimeField(auto_now_add=True)
    type_post = models.CharField(max_length=2, choices=TYPES, default=news)
    author = models.ForeignKey(Author, models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')
    header = models.CharField(max_length=128)
    text = models.TextField()
    rating_news = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.header}: {self.text} --- {self.time_post} --- {self.author.user.username}'

    def like(self):
        self.rating_news += 1
        self.save()

    def dislike(self):
        self.rating_news -= 1
        self.save()
    def preview(self):
        return f'{self.text[:124]}...'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f'post-{self.pk}')


class PostCategory(models.Model):
    post = models.ForeignKey(Post, models.CASCADE)
    category = models.ForeignKey(Category, models.CASCADE)


class Comment(models.Model):
    text_comment = models.TextField()
    time_com = models.DateTimeField(auto_now_add=True)
    rating_com = models.IntegerField(default=0)

    post = models.ForeignKey(Post, models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)

    def like(self):
        self.rating_com += 1
        self.save()

    def dislike(self):
        self.rating_com -= 1
        self.save()


