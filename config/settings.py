import os
import datetime
import dj_database_url
import environ
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
env = environ.Env()
env.read_env('.env')

SECRET_KEY = env('DJANGO_SECRET_KEY',
                 default='=wlh&01pd6h+q)*#9)gr&o2#tojutiott4p5m=iw7p^ok)@1q+')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG', default=True)
ALLOWED_HOSTS = ['*']

# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'allauth',  # registration
    'allauth.account',  # registration
    'allauth.socialaccount',
    'rest_framework',
    'rest_auth.registration',
    'rest_framework.authtoken',
    'rest_auth',
    'rest_framework_jwt',
    'corsheaders',
    'django_q',
]

LOCAL_APPS = [
    'keys',
    'meetups',
    'users',
    'estimator'
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.locale.LocaleMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {'default': env.db('DATABASE_URL', default='postgres:///creativedb')}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


# REST FRAMEWORK CONFIGURATION
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 35
}

# JWT CUSTOM DEFAULTS
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=360),
    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=360),
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
}

# Activating the Custom Serializers
REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'users.custom_registration.CustomRegistrationSerializer',
}

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'users.serializers.UserDetailModelSerializer',
    'PASSWORD_RESET_SERIALIZER': 'users.password_serializer.PasswordResetSerializer'
}


SITE_ID = 1

# Handle CORS
CORS_ORIGIN_WHITELIST = ()
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'
# DATE_INPUT_FORMATS = ('%d/%m/%Y','%Y/%m/%d')
USE_I18N = True

USE_L10N = True

USE_TZ = True

# Media root

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

# authentication defaults
ACCOUNT_ADAPTER = 'users.adapters.AccountAdapter'
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'optional'

ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 365
ACCOUNT_ALLOW_REGISTRATION = True
LOGOUT_ON_PASSWORD_CHANGE = False
LOGIN_URL = 'account_login'
AUTH_USER_MODEL = 'users.User'
REST_USE_JWT = True

# email configuration
# DEFAULT_FROM_EMAIL = 'Orders <noreply@orders.com.gh>'
# EMAIL_SUBJECT_PREFIX = 'Orders'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIL_HOST_USER = 'apikey'
# EMAIL_HOST_PASSWORD = env('SENDGRID_API_KEY', default='')
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

# if not DEBUG:
#     # S3 Setup
#     STATICFILES_DIRS = [
#         os.path.join(BASE_DIR, 'api/static'),
#     ]


# FRONTEND_URL = env('FRONTEND_URL', default='http://localhost:8081')
# ADMIN_URL = env('ADMIN_URL', default='http://localhost:8080')

# heroku specific
# django_heroku.settings(locals())

# DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)


ADMINS = [('WahabAwudu', 'wahabawudu2020@gmail.com'),]
# Logging ==========================
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#     'handlers': {
#         'console': {
#             'level': 'INFO',
#             'class': 'logging.StreamHandler',
#             'formatter': 'verbose'
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console'],
#             'level': 'DEBUG',
#             'propagate': True
#         }
#     }
# }

# sentry for loggin in production
# SENTRY_DSN = env('SENTRY_DSN', default="")
# SENTRY_LOG_LEVEL = env.int("DJANGO_SENTRY_LOG_LEVEL", default=logging.INFO)

# ENVIRONMENT = env('ENVIRONMENT', default='local')

# if not ENVIRONMENT == 'local':
#     sentry_logging = LoggingIntegration(
#         level=SENTRY_LOG_LEVEL,  # Capture info and above as breadcrumbs
#         event_level=logging.ERROR,  # Send errors as events
#     )

#     sentry_sdk.init(
#         dsn=SENTRY_DSN,
#         integrations=[sentry_logging, DjangoIntegration()],
#         # If you wish to associate users to errors (assuming you are using
#         # django.contrib.auth) you may enable sending PII data.
#         send_default_pii=True
#     )

# Q cluster settings
# Q_CLUSTER = {
#     'name': 'adesua',
#     'workers': 8,
#     'recycle': 500,
#     'timeout': 60,
#     'compress': True,
#     'save_limit': 250,
#     'queue_limit': 500,
#     'cpu_affinity': 1,
#     'label': 'Django Q',
#     'orm': 'default',
#     'error_reporting': {
#         'sentry': {
#             'dsn': SENTRY_DSN
#         }
#     }
# }


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Activate Django-Heroku.

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
