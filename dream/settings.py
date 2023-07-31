"""
Django settings for dream project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

# .env
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

# import os
# private_key = os.environ.get('PRIVATE_KEY')


from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-wdkcl%(o2#0op^ko!x6c9d503j!_c0n&h3ah)&ob01jfome)pq"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "accounts",
    "api",
    "rest_framework",
    # "rest_framework.authtoken",
    "rest_framework_simplejwt",
    "corsheaders",  # CORS
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # CORS
]

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=2),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "SIGNING_KEY": SECRET_KEY,
    "AUTH_HEADER_TYPES": ("Bearer",),
}

ROOT_URLCONF = "dream.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "dream.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.mysql',
        'NAME':'dream',
        'USER':'root',
        'PASSWORD':'',
        'HOST':'172.23.214.104',
        'PORT':'3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
#     },
# ]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Taipei"

USE_I18N = True

USE_TZ = False  # Asia/Taipei-> False, UTC -> True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "accounts.User"

AUTHENTICATION_BACKENDS = [
    "accounts.backends.UserAuthBackend",
    # "django.contrib.auth.backends.ModelBackend",
]
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",  # using admin site
        # "rest_framework.authentication.TokenAuthentication",
    ],
}


CORS_ORIGIN_ALLOW_ALL = True  # CORS

# CORS_ALLOWED_ORIGINS = [
#     'http://localhost:5501',
# ]


CORS_ALLOW_CREDENTIALS = True
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_SAMESITE = "Strict"

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5501",
    "http://127.0.0.1:5501",
    "http://192.168.166.225:5501",
    "http://172.22.95.119:5501",
]

CSRF_COOKIE_SAMESITE = "Strict"
CSRF_COOKIE_SECURE = False
# CSFR_COOKIE_DOMAIN = "localhost"

# settings.py

# Set the session engine (e.g., database-backed sessions)


# # Set a session key used for signing the session data
# SESSION_COOKIE_NAME = 'myapp_session_id'

# # Set the session age (e.g., 1 day)
# SESSION_COOKIE_AGE = 86400  # 1 day in seconds
