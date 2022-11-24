from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request 
from rest_framework import status

# serializer
from .serializers import UserSerializer, TaskSerializer

# CRUD
@api_view(['POST'])
def create_task(request: Request) -> Response:
    # getting data 
    data = request.data
    serializer = TaskSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)
    


