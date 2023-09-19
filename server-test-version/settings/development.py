from settings.common import *

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "localDB_for_testing.sqlite3",
    }
}
