import os

from settings.common import *

DEBUG = True

DATABASES = {
    # "default": {
    #     "ENGINE": "django.db.backends.sqlite3",
    #     "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    # }

    # підключення до віддаленої БД із локального середовища
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        'NAME': 'jun_emp_db',
        'USER': 'root',
        'HOST': 'dpg-ck0ttv9fp0sc73bgepp0-a.oregon-postgres.render.com',
        'PORT': '5432',
        "OPTIONS": {
            "passfile": ".my_pgpass",
        },
    }
}