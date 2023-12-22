"""
Django's settings for main project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/
 Hello, serverlesser. Which template do you like? (Use arrow keys or type to search)
> Quick start [Deploy a Hello World function to FaaS]
  Container example [Deploy function to FaaS with custom-container]
  Web Framework [Deploy a web framework to FaaS]
  Static website [Deploy a static website]
  Best practice [Experience serverless project]

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os.path
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4-djd62zr$rn#ms_qt3nceh_%o5x1(pt5uv2&lu+jns18le!m*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'simpleui',
    'rest_framework',
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

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

WSGI_APPLICATION = 'main.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "SOCKET_CONNECT_TIMEOUT": 5,  # 连接redis超时时间，单位为秒
            "SOCKET_TIMEOUT": 5,  # redis读写操作超时时间，单位为秒
        }
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR / 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR / 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ********************* 跨域配置 *****************

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_HEADERS = ('*',)

# ***************** simpleui配置 *****************
SIMPLEUI_LOGO = '/static/logo/logo.png'

SIMPLEUI_DEFAULT_THEME = 'green.css'
SIMPLEUI_DEFAULT_FONT = 14

SIMPLEUI_CONFIG = {
    'system_keep': True,
    'menu_display': ['物料信息', '库存盘点', '库存管理', '用户权限'],
    'dynamic': False,
    'menus': [
        {
            'app': 'cms',
            'name': '物料信息',
            'icon': 'fa fa-message',
            'url': 'cms/material/',
        },
        {
            'app': 'cms',
            'name': '库存盘点',
            'url': 'cms/checkinventory',
        },
        {
            'app': 'cms',
            'name': '库存管理',
            'icon': 'fa fa-cubes',
            'models': [
                {
                    'name': '入库',
                    'icon': 'fa fa-download',
                    'url': 'cms/ininventory/'
                }, {
                    'name': '出库',
                    'icon': 'fa fa-upload',
                    'url': 'cms/outinventory/'
                }
            ]
        },
        {
            'app': 'auth',
            'name': '用户权限',
            'icon': 'fa fa-user',
            'models': [
                {
                    'name': '用户',
                    'url': 'auth/user/',
                }, {
                    'name': '组',
                    'icon': 'fa fa-users',
                    'url': 'auth/group/',
                }
            ]
        }
    ]
}
