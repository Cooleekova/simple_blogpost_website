## Сайт для размещения текстовых записей (Django)

### Для запуска проекта необходимо:

Установить зависимости:

`pip install -r requirements.txt`

Cоздать базу данных в postgres и осуществить миграцию:

`python manage.py migrate`

Загрузить тестовые данные:

`python manage.py loaddata fixtures.json`

Выполнить команду:

`python manage.py runserver`
