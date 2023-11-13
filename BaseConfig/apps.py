from django.apps import AppConfig


class BaseconfigConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'BaseConfig'
    verbose_name = 'تنظیمات سایت'
