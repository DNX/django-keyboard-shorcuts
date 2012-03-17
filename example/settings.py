import os
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
os.sys.path.insert(0, os.path.dirname(PROJECT_PATH))

ADMIN_MEDIA_PREFIX = '/admin_media/'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'example.db',
    }
}
DEBUG = True
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'keyboard_shortcuts',
)
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
MEDIA_URL = '/media'
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)
ROOT_URLCONF = 'example.urls'
SECRET_KEY = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcd'
SITE_ID = 1
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
)
TEMPLATE_DEBUG = DEBUG
TEMPLATE_DIRS = (
        os.path.join(PROJECT_PATH, 'templates'),
      )
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

# START keyboard_shortcuts settings #
HOTKEYS = list()
HOTKEYS.append({'keys': 'h',
                'link': '/'})
# END keyboard_shortcuts settings #
