Адрес со всеми постами
http://127.0.0.1:8000/posts/
Поисковик
http://127.0.0.1:8000/posts/search
Детальное отображение поста
http://127.0.0.1:8000/posts/<int:pk
Создание нового поста
http://127.0.0.1:8000/posts/create
Редактирование поста
http://127.0.0.1:8000/posts/<int:pk/update
Удалить пост
http://127.0.0.1:8000/posts/<int:pk/delete
Все категории
http://127.0.0.1:8000/posts/category_list/

Задание D5.8

Логин по почте или через яндекс
http://127.0.0.1:8000/accounts/login/
Регистрация
http://127.0.0.1:8000/accounts/signup/

Все новые зарегистрированные пользователи через email добавляются в группу authors с правами на редактирование и создание постов

Аккаунты:

admin
login: admin
password: admin

Liza - профиль без прав
email: Liza@mail.ru
password: Liza123456

Dima - профиль с правами на создание/редактирование постов
email: popov@mail.ru
password: Dima123456

test - профиль с правами на создание/редактирование постов
email: test@test.com
password: Test123456

Модуль D6

1) Добавлена возможность подписаться/отписаться на категории постов, сделать это можно перейдя по ссылке категории на главном сайте ( http://127.0.0.1:8000/posts/ ), либо со страницы категорий ( http://127.0.0.1:8000/posts/category_list/ ), подписанным пользователям после публикации нового поста будет приходить на почту сообщение с ссылкой на данный пост и краткой информацией.

2) При регистрации нового пользователя на указанную почту будет приходить письмо с подтверждением регистрации.

3) Добавлен функционал запрещающий 1 автору публиковать больше 3х постов за сутки.

4) Если пользователь подписан на какую-либо категорию, то каждую неделю ему приходит на почту список новых статей, появившийся за неделю с гиперссылкой на них, чтобы пользователь мог перейти и прочесть любую из статей.

Данные почты с которой будет осуществляться рассылка новостей помещены в файл .env и добавлены в .gitignore







