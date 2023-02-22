from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import PostCategory


# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# from .models import Post
# from .tasks import send_notifications
#
#
# @receiver(post_save, sender=Post)
# def notification(sender, instance, **kwargs):
#     send_notifications.apply_async((instance.preview(), instance.id, instance.header), countdown=10)


def send_notifications(preview, pk, title, subscribers, category, username):
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/posts/{pk}',
            'username': username,
            'category': category
        }

    )

    message = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers
    )

    message.attach_alternative(html_content, 'text/html')
    message.send()


@receiver(m2m_changed, sender=PostCategory)
def notification(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.category.all()

        # Сообщения отправляются через цикл, каждому отдельному подписчику, дабы он не видел все адреса, кому
        # еще отправляются уведомления
        for category in categories:
            subscribers = category.subscribers.all()
            for subscriber in subscribers:
                email = [subscriber.email]
                username = subscriber.username

                send_notifications(
                    instance.preview(), instance.pk,
                    instance.header, email, category, username)

