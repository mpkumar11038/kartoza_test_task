"""
Django settings for user_module project.

This configuration file sets up the Django project with essential settings
such as database connection, installed apps, middleware, templates, static files,
and custom user model. It is configured for development with DEBUG enabled.

For detailed documentation, visit:
https://docs.djangoproject.com/en/5.0/topics/settings/
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

# Base directory of the project (two levels up from this file)
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y=8_a%e4$fhtv_ge)nfo7@i^$ox7f!4ytz2u=li60ry@n-r*53'

# DEBUG mode should be False in production for security reasons
DEBUG = True

# Hosts/domain names that this Django site can serve
ALLOWED_HOSTS = ['*']  # Allow all hosts during development; restrict in production

# Application definitions
INSTALLED_APPS = [
    'django.contrib.admin',          # Admin site
    'django.contrib.auth',           # Authentication framework
    'django.contrib.contenttypes',   # Content types framework
    'django.contrib.sessions',       # Session framework
    'django.contrib.messages',       # Messaging framework
    'django.contrib.staticfiles',    # Static files handling
    'django.contrib.gis',            # GeoDjango for geographic applications
    'user_app',                  # Custom app for user management
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',          # Security enhancements
    'django.contrib.sessions.middleware.SessionMiddleware',   # Session handling
    'django.middleware.common.CommonMiddleware',              # Common HTTP features
    'django.middleware.csrf.CsrfViewMiddleware',              # CSRF protection
    'django.contrib.auth.middleware.AuthenticationMiddleware',# Authentication support
    'django.contrib.messages.middleware.MessageMiddleware',   # Message framework
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # Clickjacking protection
]

# Root URL configuration module
ROOT_URLCONF = 'user_module.urls'

# Template engine configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],  # Additional directories for templates
        'APP_DIRS': True,       # Enable template loading from installed apps
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',       # Debug context
                'django.template.context_processors.request',     # Request context
                'django.contrib.auth.context_processors.auth',    # Auth context
                'django.contrib.messages.context_processors.messages', # Messages context
            ],
        },
    },
]

# WSGI application entry point
WSGI_APPLICATION = 'user_module.wsgi.application'

# Database configuration using PostGIS for spatial data support
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

# Password validation settings to enforce strong passwords
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', # Prevent passwords similar to user attributes
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', # Minimum length requirement
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', # Prevent common passwords
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', # Prevent all numeric passwords
    },
]

# Internationalization settings
LANGUAGE_CODE = 'en-us'  # Default language

TIME_ZONE = 'UTC'        # Default timezone

USE_I18N = True         # Enable Django’s translation system

USE_TZ = True           # Enable timezone-aware datetimes

# Static files (CSS, JavaScript, Images) configuration
STATIC_URL = '/static/'  # URL to access static files

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Directory where static files are collected

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Additional directories for static files during development
]

# Security setting to prevent JavaScript access to session cookie
SESSION_COOKIE_HTTPONLY = True

# Default primary key field type for models
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Use a custom user model defined in srsapp app
AUTH_USER_MODEL = 'user_app.CustomUser'

GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')  # Replace with your actual API key

LOGIN_URL = '/' # URL to redirect to for login

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}