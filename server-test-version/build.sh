#!/usr/bin/env bash

# Запуск SQL-запитів з extension.sql
psql -U root -d jun_emp_db -a -f extension.sql

# exit on error
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate