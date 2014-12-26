#-*- coding: utf-8 -*-
"""
Created by Ivan Semernyakov <direct@beatum-group.ru> on 26.12.14.
"""

#-----------------------------------------------------------------------------
# LOCAL SETTINGS
#-----------------------------------------------------------------------------

from settings import *

#-----------------------------------------------------------------------------
# DEBUG MODE
#-----------------------------------------------------------------------------

DEBUG = TEMPLATE_DEBUG = True
COMPRESS_ENABLED = False

if DEBUG:
    COMPRESS_DEBUG_TOGGLE = 'whatever'
    INTERNAL_IPS = ('127.0.0.1', 'localhost', '*')

#-----------------------------------------------------------------------------
# DATABASE
#-----------------------------------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#-----------------------------------------------------------------------------
# DEVELOPMENT CACHE
#-----------------------------------------------------------------------------

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
#     }
# }

#-----------------------------------------------------------------------------
# EMAIL
#-----------------------------------------------------------------------------

# Run dev mail server
# python -m smtpd -n -c DebuggingServer localhost:1025

if DEBUG:
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

# EMAIL_HOST = 'smtp.mail.ru'
# EMAIL_PORT = 2525
# EMAIL_HOST_USER = 'site@mysite.ru'
# EMAIL_HOST_PASSWORD = 'xxx'
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = 'site@mysite.ru'
# SERVER_EMAIL = 'site@mysite.ru'

#-----------------------------------------------------------------------------
# DEBUG TOOLBAR AND PDB
#-----------------------------------------------------------------------------

# Pass