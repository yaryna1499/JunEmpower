from settings.common import *
import os
import dj_database_url
import cloudinary


#media files storage
CLOUDINARY_STORAGE = cloudinary.config( 
  cloud_name = "dnpsnra01", 
  api_key = "635723115482662", 
  api_secret = "6w9BYka4MNPAXbhfQl7nm67D4-8" 
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

DEBUG = False
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# internal connection - локально не працює
DATABASE_URL = "postgres://root:NoKpKKicxCv1S1bihWXbOmbPvLMWPKkm@dpg-ck0ttv9fp0sc73bgepp0-a/jun_emp_db"

DATABASES = {
    "default": dj_database_url.config(
        # Feel free to alter this value to suit your needs.
        default=DATABASE_URL,
        conn_max_age=600,
    )
}
