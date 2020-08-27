from django.apps import AppConfig


class PublicationsConfig(AppConfig):
    name = 'publications'

    def ready(self):
        import publications.signals  # noqa