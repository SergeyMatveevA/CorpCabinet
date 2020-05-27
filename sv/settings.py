import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_ROOT = ''
MEDIA_URL = '/media/'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4hfx7ggep-bf-#g836lwtdsivncqs^%q%%hc9k&w*)ztphc9n!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['99.99.99.999', '99.99.99.999']

# Application definition
INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'grappelli.dashboard',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'import_export',

    'arrangement',
    'cabinet',
    'nipo_db',
    'rtk',
    'user_docs',
    'yourls',
    'yourls_interface',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sv.urls'

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

WSGI_APPLICATION = 'sv.wsgi.application'


DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'sv',
    'USER': 'sv',
    'PASSWORD': 'SV',
    'HOST': 'localhost',
    'PORT': '',
},
    'nipo': {
    'ENGINE': 'sql_server.pyodbc',
    'NAME': 'anonymous',
    'USER': 'anonymous',
    'PASSWORD': 'anonymous',
    'HOST': '192.168.50.99',
    'PORT': '',
    'OPTIONS': {
        'driver': 'ODBC Driver 17 for SQL Server',
        },
    },
    'yourls_mbr': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'anonymous',
    'USER': 'anonymous',
    'PASSWORD': 'anonymous',
    'HOST': '10.165.99.99',
    'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        }
    },
    'yourls_general': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'anonymous',
        'USER': 'anonymous',
        'PASSWORD': 'anonymous',
        'HOST': '10.165.99.99',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        }
    },
}
DATABASE_ROUTERS = ['nipo_db.router.NipoRouter', 'yourls.router.YourlsRouter']

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


LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = False

LOGIN_URL = 'admin/login/?next=/admin/'

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = '/static/'

CELERY_IMPORTS = ('sv.tasks', )
# CELERY_RESULT_BACKEND = "amqp"
CELERY_RESULT_BACKEND = 'db+postgresql://sv:SV@localhost/sv'
BROKER_URL = "amqp://admin:admin@localhost:5672/myvhost/"
BROKER_API = 'http://admin:admin@$localhost:5672/api/'
CELERY_TASK_RESULT_EXPIRES = None
# Enables error emails.
CELERY_SEND_TASK_ERROR_EMAILS = True

# Name and email addresses of recipients
ADMINS = (
    ('Sergey Matveev', 'Sergey.Matveev@anonymous.com'),
)

# Email address used as sender (From field).
SERVER_EMAIL = 'anonymous@anonymous.ru'

# Mailserver configuration
EMAIL_HOST = 'anonymous.ru'
EMAIL_PORT = 2525
EMAIL_HOST_USER = 'anonymous@anonymous.ru'
EMAIL_HOST_PASSWORD = 'anonymous'

# Настройки граппели
GRAPPELLI_ADMIN_TITLE = 'DP-Tech'
GRAPPELLI_INDEX_DASHBOARD = 'sv.dashboard.CustomIndexDashboard'
