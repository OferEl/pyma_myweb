"""
Django settings for pyma_myweb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1qvy)q#8psh79#p7_u(^uq68-%7xv3!$qd-^i3n!j@(kh_3!_p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

#TEMPLATE_DIRS = (
#    'C:/Users/oferel/workspace/pyma_myweb/template',
#)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'template'),
)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main_page',
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

ROOT_URLCONF = 'pyma_myweb.urls'

WSGI_APPLICATION = 'pyma_myweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databasesDATABASES['default'] =  dj_database_url.config()

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}



DATABASES = {'default': dj_database_url.config()}

#ON_HEROKU = os.environ.get('ON_HEROKU')
#HEROKU_SERVER = os.environ.get('HEROKU_SERVER')
#if ON_HEROKU:
#    DATABASE_URL = 'sqlite://:' + os.path.join(BASE_DIR, 'db.sqlite3','django.db.backends.sqlite3')# 'postgresql:///postgresql'
#else:
#    DATABASE_URL = 'sqlite://:' + os.path.join(BASE_DIR, 'db.sqlite3','django.db.backends.sqlite3')
#DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}



# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

#STATIC_URL = '/static/'


#STATICFILES_DIRS = (
#   os.path.join(BASE_DIR, "static"),
#)

#STATIC_ROOT = '/static/'


# Parse database configuration from $DATABASE_URL

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration

#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = '/staticfiles/'
STATIC_URL = '/static/'

#STATIC_URL = (
#    os.path.join(BASE_DIR, '/static/'),
#)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'