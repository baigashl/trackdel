from django.urls import include, path
from rest_framework import routers
from .views import LocationViewSet, import_locations

router = routers.DefaultRouter()
router.register(r'locations', LocationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('import/', import_locations, name='import'),
]
