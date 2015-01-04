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

AUTH_USER_MODEL = 'account.Account'

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

#-----------------------------------------------------------------------------
# MIDDLEWARE
#-----------------------------------------------------------------------------

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

#-----------------------------------------------------------------------------
# INSTALLED APPS
#-----------------------------------------------------------------------------

INSTALLED_APPS = (

    # Django packages
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    # External packages
    'rest_framework',

    # Internal packages
    'quick.core',
    'quick.account',
    #'quick.account.registration',
    'quick.asset',
    'quick.app.posts',

    # External packages
    'django_extensions',
    'compressor',
    'djangobower',
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

MIGRATION_MODULES = {
    'authtoken': 'authtoken.migrations',
}

# JWT_AUTH = {
#     'JWT_EXPIRATION_DELTA': datetime.timedelta(days=14),
#     'JWT_ALLOW_REFRESH': True,
#     'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=14)
# }
#
# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticated',
#     ),
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework.authentication.SessionAuthentication',
#         'rest_framework.authentication.BasicAuthentication',
#         # http://habrahabr.ru/post/243427/
#         # https://github.com/GetBlimp/django-rest-framework-jwt
#         'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
#     ),
#     'PAGINATE_BY': 10
# }

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework.authentication.SessionAuthentication',
#     )
# }

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

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