from django.apps import AppConfig


class UsersConfig(AppConfig):
    """Configuration class for 'users' app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "users"
    verbose_name = "Users"

    def ready(self) -> None:
        import users.signals
