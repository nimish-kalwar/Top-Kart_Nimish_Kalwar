from django.apps import AppConfig


class DealsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Deals'
    def ready(self):
        from Jobs import updater
        updater.start()
