from django.conf import settings
import csv
from django.db import transaction
from .models import Location

@transaction.atomic
def load_locations_from_csv(sender, **kwargs):
    file_path = settings.BASE_DIR / 'uszips.csv'
    if kwargs.get('created_models'):
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            Location.objects.all().delete()  # Очищаем таблицу перед загрузкой данных
            for row in reader:
                Location.objects.create(
                zip_code=row['zip'],
                city=row['city'],
                state=row['state_name'],
                latitude=row['lat'],
                longitude=row['lng']
                )
