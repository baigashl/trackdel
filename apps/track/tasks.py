from apps.track.models import Track, Location


def update_car_locations():
    cars = Track.objects.all()
    for car in cars:
        random_location = Location.objects.order_by('?').first()
        car.current_location = random_location
        car.save()
