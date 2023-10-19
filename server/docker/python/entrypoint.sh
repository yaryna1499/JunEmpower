#!/usr/bin/env bash

# exit on error
set -o errexit

if [ "$DATABASE" = "db_platform404" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

gunicorn --bind 0.0.0.0:8000 JunEmpower.wsgi
python manage.py makemigrations main
python manage.py migrate
python manage.py collectstatic --no-input

exec "$@"



