from rest_framework import status
from rest_framework.response import Response

from . import models, serializers


def create_track(request):
    data = request.data
    # serializer = serializers.TrackSerializer(request.data)
    # try:
    #
    # except BaseException as ex:
    #     return Response({
    #         'success': False,
    #     }, status=status.HTTP_400_BAD_REQUEST)