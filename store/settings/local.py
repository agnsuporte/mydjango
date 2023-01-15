from .base import *


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        # Or an IP Address that your DB is hosted on
        'HOST': os.environ.get('DB_HOST'),
        'PORT': '3306',
    }
}
