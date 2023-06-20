import os
import django
from django_apscheduler.jobstores import DjangoJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from apps.track.tasks import update_car_locations

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trackdel.settings")
django.setup()


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    scheduler.add_job(update_car_locations, 'interval', minutes=3)
    scheduler.start()
