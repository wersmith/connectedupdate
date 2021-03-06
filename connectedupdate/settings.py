"""
Django settings for connectedupdate project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
import os


HEROKU = True

try:
    from localflags import *
except ImportError:
    pass

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
if HEROKU:
    # Heroku specific stuff

    # SECURITY WARNING: keep the secret key used in production secret!
    # should use os.environ['SECRET_KEY'] in Production
    SECRET_KEY = os.environ['SECRET_KEY']

    # Database
    # https://docs.djangoproject.com/en/1.7/ref/settings/#databaseson
    import dj_database_url
    DATABASES={}
    DATABASES['default'] =  dj_database_url.config()


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.7/howto/static-files/

    STATIC_URL = '/static/'
    STATIC_ROOT = 'staticfiles'

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

APPEND_SLASH = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'userprofile',
    'rest_auth',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'connectedupdate.urls'

WSGI_APPLICATION = 'connectedupdate.wsgi.application'



# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PARSERP_CLASSES':('rest_framework.parsers.JSONParser'),
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',)
   #'PAGINATE_BY': 10
}

try:
    from localsettings import *
except:
    pass
