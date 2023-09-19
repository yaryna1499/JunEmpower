from settings.common import *
import os
import dj_database_url

DEBUG = False
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# internal connection - локально не працює
DATABASE_URL = "postgres://root:NoKpKKicxCv1S1bihWXbOmbPvLMWPKkm@dpg-ck0ttv9fp0sc73bgepp0-a/jun_emp_db"

DATABASES = {
    'default': dj_database_url.config(
        # Feel free to alter this value to suit your needs.
        default=DATABASE_URL,
        conn_max_age=600
    )
}


