import os
import django
from django.core.management import call_command

def before_all(context):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.settings")
    django.setup()
    call_command("migrate", verbosity=0)
