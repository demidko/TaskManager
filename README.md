# TaskManager

Проект "Менеджер задач" для университетского предмета (7 семестр) "Технологии программирования"

## Запуск при помощи [`Docker Compose`](https://www.docker.com/products/docker-desktop)

В репозитории выполните команду `docker-compose up`, уточнив логин, пароль и почту администратора, например

```
DJANGO_SUPERUSER_USERNAME=ivan \
DJANGO_SUPERUSER_PASSWORD=123456 \
DJANGO_SUPERUSER_EMAIL=ivan@ivanov.com \
docker-compose up
``` 

Сервис будет запущен на `localhost:80`. Впоследствии, для удаления всех данных Docker из системы можно использовать
команду `docker system prune -fa`.

## Запуск вручную

### Предустановка

* Установить Python. Использовалась [эта версия.](https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe)
* Установить библиотеку из консоли для виртуальных сред — `pip install virtualenv`

### Скачивание проекта, установка библиотек

1. Из консоли — `git clone https://github.com/ivanovskii/TaskManager/`
2. `cd TaskManager`
3. `virtualenv venv`
4. `venv\scripts\activate`  
   Если вы используете macOS или Linux, то вместо этого выполните команду `source venv/bin/activate`
5. `pip install -r requirements.txt`

### Настройка проекта и первый запуск

1. Поместите файл `.env` рядом с `settings.py` [опционально, но рекомендуемо]
2. Выполните миграции:

```
    python manage.py makemigrations account
    python manage.py migrate
```

3. Создайте суперпользователя командой `python manage.py createsuperuser`
4. Запустите проект командой `python manage.py runserver`
5. Перейдите на [localhost.](http://127.0.0.1:8000/)

### Последующие запуски

* Каждый раз из консоли нужно запускать `venv\scripts\activate`, `python manage.py runserver` или сконфигурировать
  запуск из IDE. Например, для VS Code это делается [так.](https://code.visualstudio.com/docs/python/tutorial-django)