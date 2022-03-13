"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv(
    'DJANGO_SECRET_KEY',
    'django-insecure-$!1l6w48lauk$*fmhbrqanz6#^s&4$@z-4^e6we4@hzlzxa6h!')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'

ALLOWED_HOSTS = os.getenv(
    'DJANGO_ALLOWED_HOSTS', 'localhost 127.0.0.1').split(' ')

INSTALLED_APPS = [
    'georga',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Packages
    'phonenumber_field',

    # GraphQL
    'graphene_django',
    'django_filters'
]

# Crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'georga.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'georga/templates',
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'georga.context_processor.main',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'georga.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.getenv(
            'DJANGO_DATABASE_ENGINE', 'django.db.backends.postgresql'),
        "HOST": os.getenv('DATABASE_HOST', '127.0.0.1'),
        "PORT": os.getenv('DATABASE_PORT', '5432'),
        "NAME": os.getenv('DATABASE_NAME', 'django'),
        "USER": os.getenv('DATABASE_USER', 'django'),
        "PASSWORD": os.getenv('DATABASE_PASSWORD', 'django'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
password_validation = 'django.contrib.auth.password_validation'
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': f'${password_validation}.UserAttributeSimilarityValidator',
    },
    {
        'NAME': f'${password_validation}.MinimumLengthValidator',
    },
    {
        'NAME': f'${password_validation}.CommonPasswordValidator',
    },
    {
        'NAME': f'${password_validation}.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "georga/static",
]

AUTHENTICATION_BACKENDS = [
    "graphql_jwt.backends.JSONWebTokenBackend",
    "django.contrib.auth.backends.ModelBackend",
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'georga.Person'

# Phonenumber fields (django-phonenumber-field)
PHONENUMBER_DEFAULT_REGION = os.getenv(
    'DJANGO_PHONENUMBER_DEFAULT_REGION', 'DE')
PHONENUMBER_DEFAULT_FORMAT = os.getenv(
    'DJANGO_PHONENUMBER_DEFAULT_FORMAT', 'INTERNATIONAL')

REPOSITORY_URL = "https://github.com/georga-app/georga-server-django"

SITE_ID = 1

# GraphQL
GRAPHENE = {
    "SCHEMA": "georga.schema_graphql.schema",
    "MIDDLEWARE": [
        "graphql_jwt.middleware.JSONWebTokenMiddleware",
    ],
}
# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('DJANGO_EMAIL_HOST', '')
EMAIL_PORT = os.getenv('DJANGO_EMAIL_PORT', '')
EMAIL_USE_TLS = os.getenv('DJANGO_EMAIL_USE_TLS', 'False') == 'True'
EMAIL_HOST_USER = os.getenv('DJANGO_EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('DJANGO_EMAIL_HOST_PASSWORD', '')
EMAIL_SENDER = os.getenv('DJANGO_EMAIL_SENDER', '')

# JWT
JWT_PRIVATE = os.getenv('DJANGO_JWT_PRIVATE_KEY', '')
JWT_PUBLIC = os.getenv('DJANGO_JWT_PUBLIC_KEY', '')

GRAPHQL_JWT = {
    'JWT_ALGORITHM': "RS256",
    'JWT_ISSUER': 'GeoRGA',
    'JWT_PUBLIC_KEY': JWT_PUBLIC,
    'JWT_PRIVATE_KEY': JWT_PRIVATE,
}

ACTIVATION_URL = os.getenv("DJANGO_ACTIVATION_URL", '')
ACTIVATION_DAYS = os.getenv('DJANGO_ACCOUNT_ACTIVATION_DAYS', '7')

PASSWORD_URL = os.getenv('DJANGO_PASSWORD_URL', '')