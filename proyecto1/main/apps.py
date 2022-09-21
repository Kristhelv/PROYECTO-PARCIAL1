from django.apps import AppConfig

#se crea la clase de configuracion.
class MainConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "main"
    def ready(self):
        import main.signals
