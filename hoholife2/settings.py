"""
Django settings for hoholife2 project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'znr0j=goi&#2bq9i*qp_%o%3++qiup^f$%-@nobk$9kn@$oxb)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['www.simple01.com','simple01.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_comments',
    'mptt',
    'tagging',
    'ckeditor_uploader',
    'ckeditor',
    # 'ckeditor_demo.demo_application',
    'zinnia',
    'zinnia_ckeditor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hoholife2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'zinnia.context_processors.version',
            ],
        },
    },
]

WSGI_APPLICATION = 'hoholife2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    #'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #},

    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'hoholife',
    'USER': 'dbushoholife',
    'PASSWORD': 'pntmdcg_game',
    'HOST': '',
    'PORT': '3306',
    },
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
#coding=utf-8

"""
Django settings for gmsite project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=!q5c#@9t9*wli&d1-p(zb5l=ull&^++hs3!#bs)8)661347s8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1','gthcn.com','www.gthcn.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'signup.apps.SignupConfig',
    'captcha',
    'django.contrib.sites',
    'polls',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'gmsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            #'debug':DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'gmsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    #'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #},
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'gthcn',    #你的数据库名称
    'USER': 'dbuser',   #你的数据库用户名
    'PASSWORD': 'pntmdcg_game', #你的数据库密码
    'HOST': '', #你的数据库主机，留空默认为localhost
    'PORT': '3306', #你的数据库端口
    },
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('en', ('English')),
    ('zh-hans', ('中文简体')),
    ('zh-hant', ('中文繁體')),
)

#翻译文件所在目录，需要手工创建
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = r'static/'

AUTH_USER_MODEL = 'signup.GameUser'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gthcn.com'           #smtp
EMAIL_PORT = 25                                 #SMTP PORT
EMAIL_HOST_USER = 'admin@gthcn.com'        #my owner mail
EMAIL_HOST_PASSWORD = 'pntmdcg_gthcn'           #my mail pwd
EMAIL_SUBJECT_PREFIX = 'GTH'            #Subject-line prefix,default:'[django]'
#EMAIL_USE_TLS = True                             #when contact with smtp server，whether enable TLS safe link. default:false
#administrator site
SERVER_EMAIL = EMAIL_HOST_USER            #The email address that error messages come from, such as those sent to ADMINS and MANAGERS.
DEFAULT_FROM_EMAIL = '女神复兴<admin@gthcn.com>'  # EMAIL_HOST_USER

#LOGIN_REDIRECT_URL = '/'

CAPTCHA_NOISE_FUNCTIONS = (
'captcha.helpers.noise_null', # 没有样式
#'captcha.helpers.noise_arcs', # 线
# 'captcha.helpers.noise_dots', # 点
)
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
CAPTCHA_LETTER_ROTATION = (-1,1)
CAPTCHA_IMAGE_SIZE = (88,30)
CAPTCHA_BACKGROUND_COLOR = '#FF98FD'
#CAPTCHA_LENGTH = 4

SITE_ID = 1


PASSWORD_HASHERS = (
    #'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    #'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    #'django.contrib.auth.hashers.Argon2PasswordHasher',
    #'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    #'django.contrib.auth.hashers.BCryptPasswordHasher',
    #'django.contrib.auth.hashers.SHA1PasswordHasher',
    #'django.contrib.auth.hashers.MD5PasswordHasher',
    #'django.contrib.auth.hashers.UnsaltedSHA1PasswordHasher',
    'django.contrib.auth.hashers.UnsaltedMD5PasswordHasher',
    #'django.contrib.auth.hashers.CryptPasswordHasher',
)

MAX_USER_AMOUNT_PER_EMAIL = 3

POST_INTERVAL_AFTER_UNFINISHED_ORDER = 600

# 未完成订单的最大数量
MAX_UNFINISHED_ORDER_AMOUNT = 3

RESET_PASSWORD_TIMES_PER_DAY = 3

MIN_USERNAME_LEN = 5
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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
# CKEDITOR_JQUERY_URL = 'js/jquery.min-2.1.1.js'

SITE_ID = 1

CKEDITOR_CONFIGS = {
    'zinnia-content': {
        'toolbar_Zinnia': [
            ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord'],
            ['Undo', 'Redo'],
            ['Scayt'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Table', 'HorizontalRule', 'SpecialChar'],
            ['CodeSnippet', 'Source'],
            ['Maximize'],
            '/',
            ['Bold', 'Italic', 'Underline', 'Strike',
             'Subscript', 'Superscript', '-', 'RemoveFormat'],
            ['NumberedList', 'BulletedList', '-',
             'Outdent', 'Indent', '-', 'Blockquote'],
            ['Styles', 'Format'],
        ],
        'toolbar': 'Zinnia',
        'extraPlugins': 'widget,lineutils,codesnippet,codemirror,selectall',
        'codeSnippet_theme': 'monokai_sublime',  # solarized_light tomorrow_night_eighties
        # 'skin': 'moono-dark',
    },
}

