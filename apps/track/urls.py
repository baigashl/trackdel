from django.urls import include, path
from rest_framework import routers
from .views import TrackCreateAPIView, TrackViewSet, RandomTrackCreateAPIView

router = routers.DefaultRouter()
router.register(r'tracks', TrackViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create/', TrackCreateAPIView.as_view(), name='create'),
    path('random/', RandomTrackCreateAPIView.as_view(), name='random-create'),
]

