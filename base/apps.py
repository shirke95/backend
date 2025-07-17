from django.apps import AppConfig


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'

    def ready(self):
        import base.signals  # Import signals to ensure they are registered
        # This will ensure that the signals are connected when the app is ready
        # You can also import other modules or perform other initialization tasks here