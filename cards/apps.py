from django.apps import AppConfig
from django.core.signals import request_finished


class CardsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "cards"

    def ready(self) -> None:
        from . import signals

        # request_finished.connect(signals.create_user_default_list_of_words)
