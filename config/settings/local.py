from .base import *
from decouple import config, Csv

DEBUG = True

ALLOWED_HOSTS = []

# for windows setup only
# DATABASES = {
#     'default': {
#         'ENGINE': config('ENGINE', default='django.db.backends.postgresql'),
#         'NAME': config('NAME', default='meetupdb'),
#         'USER': config('USER', default='postgres'),
#         'PASSWORD': config('PASSWORD', default='postgres'),
#         'HOST': config('HOST', default='127.0.0.1'),
#         'PORT': config('PORT', default='5432'),
#     }
# }
# end for windows setup only

# email configuration
DEFAULT_FROM_EMAIL = 'Meetup <noreply@meetup.com>'
EMAIL_SUBJECT_PREFIX = 'Meetup'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = '#'
EMAIL_HOST_USER = '#'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = 'Meetup <noreply@meetup.com>'
