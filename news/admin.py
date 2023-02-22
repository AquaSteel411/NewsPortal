from django.contrib import admin
from .models import Category, Post, Author, PostCategory, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'header', 'type_post', 'time_post', 'rating_news')
    list_filter = ('author', 'type_post')


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(PostCategory)
admin.site.register(Comment)
