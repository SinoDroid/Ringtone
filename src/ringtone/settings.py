#!/usr/bin/python
#-*- coding: utf-8 -*-

# Django settings for ringtone project.

import os.path

PATH_PREFIX = os.path.abspath(os.path.dirname(__file__) + '/../..')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('SinoDroid', 'sinodroid@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': PATH_PREFIX + '/res/database/sqlite/ringtone.db3',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

APPEND_SLASH = False

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = PATH_PREFIX + '/res/upload/'

MEDIA_URL = ''

STATIC_ROOT = PATH_PREFIX + '/res/media/admin/'

STATIC_URL = '/media/'

STATICFILES_DIRS = (
    PATH_PREFIX + "/res/media/",
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'c+@#e9$2^q(p(&-!ekp=^ijvn^b2(95mot-8)w6(k#97kvfln1'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.cache.CacheMiddleware',
)

#CACHES = {
#    'default' : {
#        'BACKEND' : 'django.core.cache.backends.filebased.FileBasedCache',
#        'LOCATION' : 'D:/wamp/wwwroot/.cache',
#    }
#}

ROOT_URLCONF = 'ringtone.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    #'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    #'django.contrib.admindocs',
    'ringtone.services',
    'ringtone.mobosite',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Rintone sort orders
SORT_ORDERS = {
    "popular" : "view_count",
    "recent" : "last_modify",
    "view_count" : "view_count",
    "preview_count" : "preview_count",
    "download_count" : "download_count",
    "set_as_count": "set_as_count",
}

# Default page size
DEFAULT_PAGE_SIZE = 5

# Default page number, the first page
DEFAULT_PAGE_NO = 1

# Log
import logging
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s %(levelname)s %(message)s',
)
