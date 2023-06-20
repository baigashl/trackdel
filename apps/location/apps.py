from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.db import connection
# from .utils import load_locations_from_csv


class LocationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.location'


    # def ready(self):
    #     post_migrate.connect(self.on_post_migrate, sender=self)
    #
    # def on_post_migrate(self, **kwargs):
    #     with connection.cursor() as cursor:
    #         cursor.execute("SELECT EXISTS(SELECT 1 FROM location_location)")
    #         table_exists = cursor.fetchone()[0]
    #     if not table_exists:
    #         load_locations_from_csv()

