# test_settings.py
from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': "user_info",
        'USER': "admin",
        'PASSWORD': "1",
        'HOST': "127.0.0.1",
        'PORT': "5433",
    }
}