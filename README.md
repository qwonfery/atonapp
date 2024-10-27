Этот проект - web приложение на django, реализующее функционал:
- авторизации пользователя
- получение из бд информации о клиентах, прикрепленных к пользователю, и её отображение
- изменение статуса клиента через веб интерфейс

Для запуска проекта нужно сделать следующее:
# 1
Скачать архив с проектом или загрузить с помощью команды <code>git clone https://github.com/qwonfery/atonapp </code>
# 2
Создать виртуальное окружение 
<code>py -m venv .venv</code>
Активировать виртуальное окружение
<code>.venv\Scripts\activate</code>
Загрузить зависимости
<code>py -m pip install -r requirements.txt</code>
# 3
- Команды для заполнения базы данных (по умолчанию стоит sqlite, можно изменить в settings.py)
<code>py manage.py init_db</code>

- Команда для запуска сервера 
<code>py manage.py runserver</code>

- Логином служат сочетания имен и фамилий участников битлз, примеры доступных логинов:
JohnLennon
RingoStarr
- Пароль у всех пользователей:
1

- Команда для запуска тестов 
<code>py manage.py test</code>

  
