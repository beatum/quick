#-*- coding: utf-8 -*-
"""
Django settings for quick project.
Created by Ivan Semernyakov <direct@beatum-group.ru> http://beatum-site.ru
"""

import datetime
from django.conf import global_settings

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
path = lambda *a: os.path.join(BASE_DIR, *a)

#-----------------------------------------------------------------------------
# MAIN SETTINGS
#-----------------------------------------------------------------------------

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'user.Account'

SECRET_KEY = '*=g!3f#aj8_p)dv43hvw$s512#f6&1$)j4iua9(f6x65a73&z7'

ADMINS = (
    ('Ivan Semernyakov', 'direct@beatum-group.ru'),
)

ROOT_URLCONF = 'quick.urls'

WSGI_APPLICATION = 'quick.wsgi.application'

SITE_ID = 1

#-----------------------------------------------------------------------------
# LANGUAGE, TIME-ZONE AND INTERNATIONALIZATION
#-----------------------------------------------------------------------------

TIME_ZONE = 'Europe/Moscow'

LANGUAGE_CODE = 'ru-RU'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

#-----------------------------------------------------------------------------
# STATIC AND MEDIA
#-----------------------------------------------------------------------------

MEDIA_ROOT = path('media/')

MEDIA_URL = '/media/'

STATIC_ROOT = path('static/')

STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_FINDERS = global_settings.STATICFILES_FINDERS + (
    'djangobower.finders.BowerFinder',
    'compressor.finders.CompressorFinder',
)

#-----------------------------------------------------------------------------
# TEMPLATES
#-----------------------------------------------------------------------------

TEMPLATE_DIRS = (
    path('templates'),
)

TEMPLATE_LOADERS = (
    'hamlpy.template.loaders.HamlPyFilesystemLoader',
    'hamlpy.template.loaders.HamlPyAppDirectoriesLoader',
) + global_settings.TEMPLATE_LOADERS

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

#-----------------------------------------------------------------------------
# MIDDLEWARE
#-----------------------------------------------------------------------------

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

#-----------------------------------------------------------------------------
# INSTALLED APPS
#-----------------------------------------------------------------------------

INSTALLED_APPS = (

    # Django packages
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.humanize',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',

    # External packages
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'rest_framework',
    'rest_framework.authtoken',
    'django_extensions',
    'compressor',
    'djangobower',

    # Internal packages
    'quick.core',
    'quick.asset',
    'quick.user',
    'quick.user.registration',
    'quick.app.posts',
)

#-----------------------------------------------------------------------------
# COMPRESS
#-----------------------------------------------------------------------------

COMPRESS_URL = '/'

COMPRESS_ROOT = BASE_DIR

COMPRESS_OUTPUT_DIR = 'media/compress'

COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile}'),
    ('text/x-scss', 'sass --scss {infile} {outfile}'),
    ('text/x-sass', 'sass {infile} {outfile}'),
)

#-----------------------------------------------------------------------------
# DJANGO REST FRAMEWORK
#-----------------------------------------------------------------------------

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'PAGINATE_BY': 10
}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

#-----------------------------------------------------------------------------
# ACCOUNT
#-----------------------------------------------------------------------------

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_AUTHENTICATION_METHOD = 'email'

ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

ACCOUNT_ACTIVATION_DAYS = 1

#-----------------------------------------------------------------------------
# BOWER
#-----------------------------------------------------------------------------

BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'components')

BOWER_INSTALLED_APPS = (
    'snackbarjs#1.0.0',
    'underscore#1.7.0',
    'ngDialog#0.3.8',
    'bootstrap-material-design#0.2.1',
    'angular-resource#1.3.8',
    'angular-cookies#1.3.8',
    'angular#1.3.8',
    'bootstrap#3.3.1',
    'angular-animate#1.3.8',
    'angular-mocks#1.3.8',
    'jquery#2.1.3',
    'angular-route#1.3.8'
)

#----------------------------------------------------------------------------
# LOCAL SETTINGS
#-----------------------------------------------------------------------------

try:
    from settings_local import *
except ImportError:
    pass