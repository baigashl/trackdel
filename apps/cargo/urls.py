from django.urls import include, path
from rest_framework import routers
from .views import CargoViewSet, CargoCreateAPIView

router = routers.DefaultRouter()
router.register(r'cargos', CargoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create/', CargoCreateAPIView.as_view(), name='cargo'),
]
