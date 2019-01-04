from .settings import *

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_auth',
    'django_allauth',

    'django.contrib.sites', # for allauth
    'allauth',  # for allauth
    'allauth.account',  # for allauth
    'allauth.socialaccount',    # for allauth
    'allauth.socialaccount.providers.facebook',  # for allauth
    'allauth.socialaccount.providers.google',    # for allauth
    'allauth.socialaccount.providers.twitter',   # for allauth
    'django_extensions'
]
print(os.path.join(BASE_DIR, 'apps/django_allauth/templates'))

SITE_ID = 1

ROOT_URLCONF = 'authorization.urls_allauth'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(BASE_DIR,'apps/django_allauth/templates')],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE':'django.db.backends.mysql',
        'NAME':'authorization',
        'USER':'root',
        'PASSWORD': 'root',
        'PORT': '',
        'HOST': ''

    }
}




AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

LOGIN_REDIRECT_URL = '/'

# ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True   #  The user is required to hand over an e-mail address when signing up.

#   Determines the e-mail verification method during signup – choose one of "mandatory", "optional",
#   or "none". When set to “mandatory” the user is blocked from logging in until the email
#   address is verified.
ACCOUNT_EMAIL_VERIFICATION = "mandatory"

#   Request e-mail address from 3rd party account provider? E.g. using OpenID AX,
#   or the Facebook “email” permission.
SOCIALACCOUNT_QUERY_EMAIL = ACCOUNT_EMAIL_REQUIRED

