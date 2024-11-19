from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, api_view
from .serializer import BlogSerializers
from rest_framework import status
from .models import Blog
# Create your views here.


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_blog(request):
  serializer = BlogSerializers(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  else:
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_blogs(request):
  blogs = Blog.objects.all()
  serializer = BlogSerializers(blogs, many=True)
  return Response(serializer.data)