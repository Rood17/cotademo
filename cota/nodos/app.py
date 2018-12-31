from django.apps import AppConfig

from dal.test.utils import fixtures
from django.db.models.signals import post_migrate

class NodosConfig(AppConfig):
    name = 'nodos'
    verbose_name='Librería'

    # Many2Many
    def ready(self):
        post_migrate.connect(fixtures, sender=self)


