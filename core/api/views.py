from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.models import Room
from .serializers import RoomSerializer


@api_view(['GET'])
def getRoutes(request):
    routers = [
        'GET /api'
        'GET /api/rooms',
        'GET /api/rooms/:id',
    ]
    return Response(routers)

@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(request, pk):
    rooms = Room.objects.get(id=pk)
    serializer = RoomSerializer(rooms, many=False)
    return Response(serializer.data)