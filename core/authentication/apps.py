from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.authentication'

    def ready(self):
        try:
            import core.authentication.signals.user
        except Exception as e:
            print(f"Erro ao carregar signals: {e}")