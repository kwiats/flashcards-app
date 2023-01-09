from django.apps import AppConfig


class TranslationsConfig(AppConfig):
    """Configuration class for the 'translations' app"""

    default_auto_field = "django.db.models.BigAutoField"

    name = "apps.translations"
    verbose_name = "Translations for word"
