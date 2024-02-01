from django.apps import AppConfig


class SelPreRelatedConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sel_pre_related"

    def ready(self):
        import sel_pre_related.signals
