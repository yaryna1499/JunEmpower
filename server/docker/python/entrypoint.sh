#!/usr/bin/env bash

# exit on error
set -o errexit


gunicorn --bind 0.0.0.0:8000 JunEmpower.wsgi
python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate





