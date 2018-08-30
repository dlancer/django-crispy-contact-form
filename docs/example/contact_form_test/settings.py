"""
Django settings for contact_form_test project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yynb@_sv#f5lq(zlxuq#%w7$n4_6g*7zoc6z3(ju-_ph*3rseb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEBUG_TOOLBAR = True

ALLOWED_HOSTS = []

SITE_ID = 1

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # optional
    # 'modeltranslation',
    'captcha',
    'crispy_forms',
    'contact_form',
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# Templates settings
TPL_DIRS = tuple([os.path.join(BASE_DIR, app_name, 'templates') for app_name in INSTALLED_APPS])
TPL_DIRS += tuple([os.path.join(BASE_DIR, 'templates')])

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TPL_DIRS,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG
        },
    },
]

ROOT_URLCONF = 'contact_form_test.urls'

WSGI_APPLICATION = 'contact_form_test.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

gettext = lambda s: s
LANGUAGES = (
    ('en', gettext('English')),
    ('ru', gettext('Russian')),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

CRISPY_TEMPLATE_PACK = 'uni_form'

# captcha settings
CAPTCHA_FONT_PATH = os.path.join(BASE_DIR, '_fonts/DroidSans.ttf')
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'
CAPTCHA_LETTER_ROTATION = (-5, 5)
CAPTCHA_FOREGROUND_COLOR = '#201500'
CAPTCHA_NOISE_FUNCTIONS = ('captcha.helpers.noise_dots',)

CONTACT_FORM_USE_CAPTCHA = True
CONTACT_FORM_USE_SIGNALS = True
CONTACT_FORM_USE_SITES = False
CONTACT_FORM_MIN_MESSAGE_LENGTH = 30
# CONTACT_FORM_SUCCESS_URL = '/'
