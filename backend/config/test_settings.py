from config.settings import *  # noqa
from dotenv import dotenv_values

env = dotenv_values(".env")

SECRET_KEY = env["SECRET_KEY"]


TEST_RUNNER = "django.test.runner.DiscoverRunner"


PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]


EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

DEBUG = True  # type: ignore # noqa F405
