# import datetime
#
# from celery import shared_task
# from django.conf import settings
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string
#
# from .models import Post, Category
#
#
# @shared_task
# def weekly_email():
#     today = datetime.datetime.now()
#     last_week = today - datetime.timedelta(days=7)
#     posts = Post.objects.filter(time_post__gte=last_week)
#     categories = set(posts.values_list('category__topic', flat=True))
#     subscribers = set(Category.objects.filter(topic__in=categories).values_list('subscribers__email', flat=True))
#
#     html_content = render_to_string(
#         'daily_posts.html',
#         {
#             'link': settings.SITE_URL,
#             'posts': posts,
#         }
#     )
#
#     message = EmailMultiAlternatives(
#         subject='Статьи за неделю',
#         body='',
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         to=subscribers
#     )
#
#     message.attach_alternative(html_content, 'text/html')
#     message.send()
#
#
# @shared_task()
# def send_notifications(preview, id, title):
#     post = Post.objects.get(pk=id)
#     categories = post.category.all()
#
#     for category in categories:
#         subscribers = category.subscribers.all()
#         for subscriber in subscribers:
#             email = [subscriber.email]
#             username = subscriber.username
#
#             html_content = render_to_string(
#                 'post_created_email.html',
#                 {
#                     'text': preview,
#                     'link': f'{settings.SITE_URL}/posts/{id}',
#                     'username': username,
#                     'category': category
#                 }
#
#             )
#
#             message = EmailMultiAlternatives(
#                 subject=title,
#                 body='',
#                 from_email=settings.DEFAULT_FROM_EMAIL,
#                 to=email
#             )
#
#             message.attach_alternative(html_content, 'text/html')
#             message.send()
