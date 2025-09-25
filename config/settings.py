"""
Configuration settings for the IAM tool demo
"""

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'iam_demo',
        'USER': 'admin',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# API settings
API_VERSION = 'v1'
DEBUG = True
SECRET_KEY = 'your-secret-key-here'

# Authentication settings
AUTHENTICATION_BACKENDS = [
    'account.backends.CustomModelBackend',
    'account.backends.TokenBackend',
]

# Application definition
INSTALLED_APPS = [
    'account',
    'api',
    'common',
]

MIDDLEWARE = [
    'common.middlewares.AuthenticationMiddleware',
    'common.middlewares.LoggingMiddleware',
]