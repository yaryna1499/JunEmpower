import os
import dj_database_url
from settings.common import *

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
    # підключення до віддаленої БД із локального середовища
    # "default": dj_database_url.config(
    #     # Feel free to alter this value to suit your needs.
    #     default="postgres://root:NoKpKKicxCv1S1bihWXbOmbPvLMWPKkm@dpg-ck0ttv9fp0sc73bgepp0-a.oregon-postgres.render.com/jun_emp_db",
    #     conn_max_age=600,
    # )
}
