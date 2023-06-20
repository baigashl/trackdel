import csv
from .models import Location


def load_locations_from_csv(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            Location.objects.create(
                zip_code=row['zip'],
                city=row['city'],
                state=row['state_name'],
                latitude=row['lat'],
                longitude=row['lng']
            )
