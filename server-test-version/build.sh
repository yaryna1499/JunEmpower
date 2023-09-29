#!/usr/bin/env bash



# exit on error
set -o errexit

# Запуск SQL-запитів з extension.sql
PGPASSWORD=NoKpKKicxCv1S1bihWXbOmbPvLMWPKkm psql -h dpg-ck0ttv9fp0sc73bgepp0-a -U root jun_emp_db -a -f extension.sql
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate