from pathlib import Path
import os
from dotenv import load_dotenv
from datetime import timedelta
import cloudinary
from urllib.parse import urlparse

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')

MODE = os.getenv("MODE", "DEVELOPMENT")

DEBUG = os.getenv('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = ["https://fabrica-portal-backend.fexcompany.me", "http://localhost:8000", "http://127.0.1:8000"]

APPEND_SLASH = False

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django_celery_results",
    'rest_framework',
    'rest_framework_simplejwt',
    'core.uploader',
    'core.authentication',
    'core.portal',
    "core",
    "corsheaders",
    'django_filters',
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = 'django_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_project.wsgi.application'

DATABASE_URL = urlparse(os.getenv("DATABASE_URL"))

if MODE in ["PRODUCTION", "MIGRATE"]:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": DATABASE_URL.path.replace("/", ""),
            "USER": DATABASE_URL.username,
            "PASSWORD": DATABASE_URL.password,
            "HOST": DATABASE_URL.hostname,
            "PORT": 5432,
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
        "DEFAULT_PERMISSION_CLASSES": [
        'django_project.permission.CustomGeneralPermission',  
    ]
}


AUTH_USER_MODEL = 'authentication.User'

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
}


EMAIL_BACKEND = os.getenv("EMAIL_BACKEND")
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "fabricadesoftware.araquari@ifc.edu.br")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")

CELERY_BROKER_URL = os.getenv("RABBITMQ_URL")

CELERY_RESULT_BACKEND = "django-db"

CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"

CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True

CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True

TASK_ALWAYS_EAGER = False

CELERY_TASK_QUEUES = {
    'emails': {
        'exchange': 'emails',
        'routing_key': 'emails',
        'queue_arguments': {'x-max-priority': 10, 'x-message-ttl': 60000}
    }
}

CELERY_TASK_DEFAULT_QUEUE = 'emails'
CELERY_TASK_DEFAULT_EXCHANGE = 'emails'
CELERY_TASK_DEFAULT_ROUTING_KEY = 'emails'


CORS_ALLOW_ALL_ORIGINS = True 
CORS_ALLOW_CREDENTIALS = True  


CORS_ALLOW_HEADERS = [
    'authorization',
    'content-type',
    'x-requested-with',
    'accept',
    'origin',
    'x-csrftoken',
]  

CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS'
]  

CLOUD_NAME = os.getenv('CLOUD_NAME')
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

cloudinary.config(
    cloud_name=CLOUD_NAME,
    api_key=API_KEY,
    api_secret=API_SECRET
)

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_STORAGE = os.getenv("STATICFILES_STORAGE")