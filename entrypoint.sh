#!/bin/sh

# Ждём, пока PostgreSQL запустится
echo "Waiting for PostgreSQL..."
while ! nc -z $DB_HOST $DB_PORT; do
    sleep 0.1
done
echo "PostgreSQL started"

# Выполняем миграции
python manage.py migrate

# Собираем статику
python manage.py collectstatic --noinput

# Запускаем команду
exec "$@"
