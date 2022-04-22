from pathlib import Path
import os
from datetime import timedelta
from proyectoa_agenda.credenciales import clave,correo


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-tk%c(=%d)ygd25@%11tj_2ujw+7ry!(t$=jae97v6jht%e9@-f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_bootstrap5',
    'widget_tweaks',    
	'app_contactos',
    'verificacion',
    'captcha',
    'axes',
]

AUTHENTICATION_BACKENDS = [
'axes.backends.AxesBackend',
'django.contrib.auth.backends.ModelBackend',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.AxesMiddleware',
    
]

ROOT_URLCONF = 'proyectoa_agenda.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['','C:/Users/legen/Downloads/ProyectoA_App_Web_Agenda_Contactos_Django_Python/ProyectoA_App_Web_Agenda_Contactos_Django_Python/verificacion/templates'],
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

WSGI_APPLICATION = 'proyectoa_agenda.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':'dbpr4',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Password validation
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
LANGUAGE_CODE = 'es-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Ruta para las imágenes de cada registro
MEDIA_URL = '/app_contactos/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'app_contactos/static/fotos')
 
# Activar 'CookieStorage' para enviar los mensajes de respuesta al Crear, Eliminar y Actualizar un registro
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_FILE_PATH = BASE_DIR / "sent_emails"
EMAIL_BACKEND="django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST="smtp.gmail.com"
EMAIL_USE_TLS=True
EMAIL_PORT=587
EMAIL_HOST_USER=correo
EMAIL_HOST_PASSWORD=clave

delta = timedelta( 
    days=0,
    seconds=0,
    microseconds=0,
    milliseconds=0,
    minutes=0,
    hours=1,
    weeks=0
)

AXES_ENABLED = True
AXES_FAILURE_LIMIT = 6
AXES_LOCK_OUT_AT_FAILURE=False
AXES_ONLY_USER_FAILURES=True
AXES_COOLOFF_TIME=delta
AXES_LOCKOUT_TEMPLATE='suspendida.html'
AXES_HANDLER = 'axes.handlers.database.AxesDatabaseHandler'
 