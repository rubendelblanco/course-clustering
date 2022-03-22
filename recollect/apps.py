from django.apps import AppConfig
from recollect.management import *


class RecollectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recollect'
