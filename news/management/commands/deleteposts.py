from django.core.management.base import BaseCommand
from news.models import Post, Category


class Command(BaseCommand):
    help = 'Название категории пишется с заглавной буквы'
    missing_args_message = 'Недостаточно аргументов'
    requires_migrations_checks = True

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        if options['category'] not in Category.objects.all().values_list('topic', flat=True):
            self.stdout.write(self.style.ERROR(f'Категории {options["category"]} не существует!'))
            return
        self.stdout.readable()
        self.stdout.write(f'Вы действительно хотите удалить все посты категории {options["category"]}? y/n')
        answer = input()

        if answer == 'y':
            Post.objects.filter(category__topic=options['category']).delete()

            self.stdout.write(self.style.SUCCESS('Удаление прошло успешно!'))
            return

        self.stdout.write(self.style.ERROR('Удаление прервано...'))
