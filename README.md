# Задание для UpTrader

Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:

1. Меню реализовано через template tag
2. Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3. Хранится в БД.
4. Редактируется в стандартной админке Django
5. Активный пункт меню определяется исходя из URL текущей страницы
   6 )Меню на одной странице может быть несколько. Они определяются по названию.
6. При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
   8)На отрисовку каждого меню требуется ровно 1 запрос к БД
   Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.
   {% draw_menu 'main_menu' %}
   При выполнении задания из библиотек следует использовать только Django и стандартную библиотеку Python.

## Для тго что бы не вносить данные, предворительно надо прописать эти команды:

`python3 manage.py migrate`
`py tree_navbar/manage.py loaddata db.json`

## .env файл должен выглядить так:

`DEBUG = True`
`SECRET_KEY ='SECRET_KEY'`


## Пользователь в нем уже есть 
Login - re
password - 123
