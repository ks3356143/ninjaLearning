import os
from datetime import timedelta
from pathlib import Path
from conf.env import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1e=-@5kcu))b6g7(*u+5dykk3pr0dkznrt+!))%7vf*tu#pxfn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = locals().get('DEBUG', True)
ALLOWED_HOSTS = locals().get('ALLOWED_HOSTS', ['*'])
DEMO = locals().get('DEMO', False)

# Application definition

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_celery_beat',
    'django_celery_results',
    'ninjaapp', # 创建的app一号
    'ninja', # 添加到这里便于在前端接口页面加载快一点
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 设置主路由
ROOT_URLCONF = 'ninjiaDemo.urls'

# 接口模式不变
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

# 也不用设置
WSGI_APPLICATION = 'ninjiaDemo.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
# 数据库配置
if DATABASE_TYPE == "MYSQL":
    # Mysql数据库
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "HOST": DATABASE_HOST,
            "PORT": DATABASE_PORT,
            "USER": DATABASE_USER,
            "PASSWORD": DATABASE_PASSWORD,
            "NAME": DATABASE_NAME,
        }
    }
elif DATABASE_TYPE == "SQLSERVER":
    # SqlServer数据库
    DATABASES = {
        "default": {
            "ENGINE": "mssql",
            "HOST": DATABASE_HOST,
            "PORT": DATABASE_PORT,
            "USER": DATABASE_USER,
            "PASSWORD": DATABASE_PASSWORD,
            "NAME": DATABASE_NAME,
            # 全局开启事务，绑定的是http请求响应整个过程
            'ATOMIC_REQUESTS': True,
            'OPTIONS': {
                'driver': 'ODBC Driver 17 for SQL Server',
            },
        }
    }
else:
    # sqlite3 数据库
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            'OPTIONS': {
                'timeout': 20,
            },
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'ninjaapp.Users'
USERNAME_FIELD = 'username'
ALL_MODELS_OBJECTS = []  # 所有app models 对象


# token 有效时间 时 分 秒
TOKEN_LIFETIME = 12 * 60 * 60
# TOKEN_LIFETIME = 50