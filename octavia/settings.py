"""
Django settings for teacompanocis project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
import ssl
import logging
import django_heroku
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Define la ruta absoluta a la carpeta de imágenes
IMAGE_FOLDER = os.path.join(BASE_DIR, 'static', 'images')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-og56)sheg&mr2jx)s3$2o(c7w7&eneghk2ds1b(vh(u1x!y&5v"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['https://octavialingerie-771ec71cf6aa.herokuapp.com/', '127.0.0.1', 'localhost', '127.0.0.1:8000']

# Amazon info
load_dotenv()
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = 'teacompano-img'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_REGION_NAME = 'us-east-2'
AWS_DEFAULT_ACL = 'public-read'
USE_I18N = True

# Api keys of mercadopagos
MERCADOPAGO_URL = "https://api.mercadopago.com/v1/payments/"
MERCADOPAGO_PUBLIC_KEY = "APP_USR-3631e183-eff4-474e-8f32-704eccc16578"
MERCADOPAGO_ACCESS_TOKEN = "APP_USR-1611010299166741-092904-c7a74b63ba851707b3925261263f3ed4-652583311"
MERCADOPAGO_CLIENT_ID = "1611010299166741"
MERCADOPAGO_CLIENT_SECRET = "CCrznaGLOIf33iM6arHjHFP5hlhv7FAv"
""" 
if DEBUG:
    MERCADOPAGO_PUBLIC_KEY = os.environ.get("MERCADOPAGO_PUBLIC_KEY_TEST")
    MERCADOPAGO_ACCESS_TOKEN = os.environ.get("MERCADOPAGO_ACCESS_TOKEN_TEST") """


# Api keys of wompi
WOMPI_PUBLIC_KEY = os.environ.get("WOMPI_PUBLIC_KEY_PROD")
WOMPI_PRIVATE_KEY = os.environ.get("WOMPI_PRIVATE_KEY_PROD")

if DEBUG:
    WOMPI_PUBLIC_KEY = os.environ.get("WOMPI_PUBLIC_KEY_TEST")
    WOMPI_PRIVATE_KEY = os.environ.get("WOMPI_PRIVATE_KEY_TEST")


# Api keys of epayco
EPAYCO_PUBLIC_KEY = os.environ.get("EPAYCO_PUBLIC_KEY_PROD")

if DEBUG:
    EPAYCO_PUBLIC_KEY = os.environ.get("EPAYCO_PUBLIC_KEY_TEST")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django_extensions",
    "rangefilter",
    "sorl.thumbnail",
    "storages",
    "octavia",
    "octavia.apps",
    "octavia.apps.clientes",
    "octavia.apps.inventario",
    "octavia.apps.ventas",
    "octavia.apps.navegacion",
    "django_celery_results",
    "django_celery_beat",
    "ckeditor"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "octavia.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "octavia.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        #"ENGINE": "django.db.backends.sqlite3",
        #"NAME": BASE_DIR / "db.sqlite3",
        'ENGINE': 'django.db.backends.postgresql',
        #'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = "uploads"

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

try:
    from .local_settings import *  # noqa
except ImportError:
    pass

django_heroku.settings(locals())

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'django.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    },
}
