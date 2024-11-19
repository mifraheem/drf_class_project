from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from django.contrib.auth.hashers import make_password

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    # get user
    user = request.user
    print(user.username)
    print('*'*29)
    content = {
        'status': 'request was permitted'
    }
    return Response(content)



@api_view(['POST'])
def regsiter_user(request):
    data = request.data
    print(data)
    print("**************")
    if 'password' in data:
        data['password'] = make_password(data['password'])

    serializer = UserSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


