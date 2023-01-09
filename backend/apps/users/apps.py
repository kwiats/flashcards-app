from django.apps import AppConfig


class UsersConfig(AppConfig):
    """Configuration class for 'users' app."""

    name = "apps.users"
    verbose_name = "Users"

    def ready(self) -> None:
        import apps.users.signals  # noqa
