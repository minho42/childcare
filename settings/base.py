from pathlib import Path

import dj_database_url
import environ

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = env("CHILDCAREAPP_SECRET_KEY")

DEBUG = env("DEBUG")

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]
# <-- added for bebug_toolbar to appear
INTERNAL_IPS = ["localhost", "127.0.0.1"]

INSTALLED_APPS = [
    "django.contrib.sites",
    "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    # third party apps
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    "django_celery_beat",
    # local apps
    "childcare",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # The WhiteNoise middleware should be placed directly after the Django SecurityMiddleware and before all other middleware
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # `allauth` needs this from django
                "django.template.context_processors.request",
                # this allows navbar.html to access {{ MEDIA_URL }}
                "django.template.context_processors.media",
            ]
        },
    }
]

AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)

CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = (
    "http://localhost:3000",
    "https://127.0.0.1:8080",
    "https://127.0.0.1:8000",
    "https://childcares.netlify.app",
)

REST_FRAMEWORK = {
    # "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticatedOrReadOnly"],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        # "rest_framework_simplejwt.authentication.JWTAuthentication",
        # "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
}

SITE_ID = 1

WSGI_APPLICATION = "project.wsgi.application"

DATABASES = {
    "default": dj_database_url.config(
        # default=env("DATABASE_URL"), 
        conn_max_age=600,
        # conn_health_checks=True, 
        ssl_require=True)
}

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "childcareapp",
#         "USER": "childcareappuser",
#         "PASSWORD": env("CHILDCAREAPP_DB_PASSWORD"),
#         "HOST": "localhost",
#         "PORT": "5432",
#     }
#     # "default": {
#     #     "ENGINE": "django.db.backends.sqlite3",
#     #     "NAME": "childcare_database"
#     # }
# }

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


LANGUAGE_CODE = "en-us"

# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
TIME_ZONE = "Australia/Sydney"

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
# http://whitenoise.evans.io/en/stable/django.html
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = ""
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_PORT = "587"
EMAIL_USE_TLS = True

# CELERY STUFF
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
# CELERY_ENABLE_UTC = True
CELERY_TIMEZONE = "Australia/ACT"
CELERY_TASK_SOFT_TIME_LIMIT = 900


# https://django-csp.readthedocs.io/en/latest/
# https: // github.com/mozilla/django-csp
# django-csp, Content-Security-Policy
CSP_DEFAULT_SRC = ("'none'",)
# CSP_STYLE_SRC = ("'self'", "https://use.fontawesome.com", "https://code.jquery.com",
#                  "https://cdnjs.cloudflare.com/ajax/", "https://stackpath.bootstrapcdn.com/bootstrap", "https://code.jquery.com", "https://cdn.jsdelivr.net/npm/vue@2.6.0")
# CSP_SCRIPT_SRC_ELEM = ("'self'", "https://code.jquery.com")
# CSP_SCRIPT_SRC = ("'self'", "https://cdnjs.cloudflare.com/ajax/", )
CSP_IMG_SRC = ("'self'",)
CSP_FONT_SRC = ("'self'",)


CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379"

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
