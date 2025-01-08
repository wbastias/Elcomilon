from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
    # es para colocar el nombre a la app en ves de app ternomarket
    verbose_name = "tecnomarket"
