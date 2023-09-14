from settings.common import *

DEBUG = False

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')