from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
import random
from rest_framework.views import APIView
from django.views import generic
from rest_framework import viewsets, status
from .models import Track
from rest_framework.permissions import AllowAny
from .serializers import TrackSerializer
from apps.location.models import Location
from .logic import create_track


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


def generate_unique_number():
    number = random.randint(1000, 9999)
    letter = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return str(number) + letter


def generate_random_location():
    locations = Location.objects.all()
    random_choice = random.choice(locations)
    return random_choice


class RandomTrackCreateAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        while True:
            uniq_num = generate_unique_number()
            if not Track.objects.filter(unique_number=uniq_num).exists():
                random_location = generate_random_location()
                track = Track.objects.create(
                    unique_number=uniq_num,
                    current_location=random_location,
                    carrying_capacity=random.randint(1, 1000),
                )
                track.save()
                break
            else:
                continue
        return Response({'response': 'Random Track created!'}, status=status.HTTP_201_CREATED)


class TrackCreateAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = TrackSerializer(data=request.data)

        if Track.objects.filter(unique_number=request.data['unique_number']).exists():
            return Response({'response': 'Track number already exists'})
        else:
            if serializer.is_valid():
                location = Track.objects.create(
                    unique_number=request.data['unique_number'],
                    current_location=request.data['current_location'],
                    carrying_capacity=request.data['carrying_capacity'],
                )
                location.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    pagination_class = StandardResultsSetPagination
