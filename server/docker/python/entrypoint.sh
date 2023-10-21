#!/usr/bin/env bash

# exit on error
set -o errexit

# Вказати шлях до .env файлу
ENV_FILE_PATH=".env"

# Перевірити, чи існує файл .env
if [ -f "$ENV_FILE_PATH" ]; then
  # Завантажити змінні з файлу .env
  source "$ENV_FILE_PATH"
else
  echo "Файл .env не знайдено в $ENV_FILE_PATH"
  exit 1
fi

# Очікування на PostgreSQL
if [ "$POSTGRES_DB" = "db_platform404" ]; then
  echo "Waiting for postgres..."

  while ! nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
    sleep 0.1
  done

  echo "PostgreSQL started"
fi

# Запуск міграцій
python manage.py makemigrations main
python manage.py migrate
python manage.py collectstatic --no-input

# Запуск Gunicorn
gunicorn --bind 0.0.0.0:8000 JunEmpower.wsgi

# Заміна процесу скрипта із збереженням аргументів
exec "$@"
