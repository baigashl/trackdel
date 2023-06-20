from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .models import Cargo
from apps.location.models import Location
from .serializers import CargoSerializer


class CargoCreateAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CargoSerializer(data=request.data)
        if serializer.is_valid():
            delivery = Location.objects.get(zip_code=request.data['delivery'])
            pick_up = Location.objects.get(zip_code=request.data['pick_up'])
            print(delivery)
            cargo = Cargo.objects.create(
                pick_up=delivery,
                delivery=pick_up,
                weight=request.data['weight'],
                description=request.data['description'],
            )
            cargo.save()
            ser = CargoSerializer(cargo)
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
