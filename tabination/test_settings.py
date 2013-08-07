import django


if django.VERSION[:2] >= (1, 3):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    }
else:
    DATABASE_ENGINE = 'sqlite3'

INSTALLED_APPS = [
    'tabination',
]

SECRET_KEY = "kvi0q_snk4a0fd*&amp;tvx)klm@($x^)g+nlw-+y7@e)6$1xm6!ql"

ROOT_URLCONF = 'tabination.test_urls'

TEST_RUNNER = 'discover_runner.DiscoverRunner'
