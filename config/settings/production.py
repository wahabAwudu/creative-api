from .base import *
from decouple import config, Csv
import django_heroku
import dj_database_url


DEBUG = False

ALLOWED_HOSTS = ['*']

# django whitenoise for staticfiles in production
MIDDLEWARE += (
  'whitenoise.middleware.WhiteNoiseMiddleware',
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# redis caches
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            'IGNORE_EXCEPTIONS': True,
        }
    }
}

# email configuration
# EMAIL_SUBJECT_PREFIX = 'Meetup'
# SERVER_EMAIL = 'Meetup'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIL_HOST_PASSWORD = config('SENDGRID_USERNAME')
# EMAIL_HOST_USER = config('SENDGRID_PASSWORD')
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

# DEFAULT_FROM_EMAIL = 'Meetup <noreply@meetup.com>'

# heroku specific
django_heroku.settings(locals())

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)