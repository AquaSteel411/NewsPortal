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




