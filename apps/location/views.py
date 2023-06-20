from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Location
from .serializers import LocationSerializer
from .models import Location
from django.http import HttpResponse
from .loacations_import import load_locations_from_csv
from django.conf import settings


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    pagination_class = StandardResultsSetPagination


def import_locations(request):
    file_path = settings.BASE_DIR / 'uszips.csv'
    load_locations_from_csv(file_path)
    return HttpResponse('Locations imported successfully.')
