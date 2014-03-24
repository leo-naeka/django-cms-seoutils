import os

PROJECT_DIR = os.path.dirname(__file__)

SECRET_KEY = 'x' * 20

INSTALLED_APPS = (
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'cms_seoutils',  # BEFORE sitemaps
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'mptt',
    'menus',
    'south',
    'sekizai',
    'reversion',
)

gettext = lambda x: x

LANGUAGES = (
    ('en', gettext('English')),
    ('it', gettext('Italian')),
    ('de', gettext('Deutsch'))
    )

LANGUAGE_CODE = 'en'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.filesystem.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

STATIC_URL = '/assets/static/'
MEDIA_URL = '/assets/media/'
SITE_ID = 1

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'data/db.sqlite'
    }
}

CMS_TEMPLATES = (
    ('empty.html', 'Empty'),
    ('page.html', 'Page'),
)

ROOT_URLCONF = 'cms_seoutils.test_utils.urls.py'
