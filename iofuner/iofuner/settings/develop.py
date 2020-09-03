from .base import *    #NOQA

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'iofuner',
        'HOST': '127.0.0.1',
        'USER': 'root',
        'PORT': '21246',
        'PASSWORD': 'C5O0yfjH&Q*0',
    }
}