from django.shortcuts import render
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Product
# Create your views here.


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_product(request):
  data = request.data
  data['seller'] = request.user.id

  serializer = ProductSerializer(data=data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  else:
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_products(request):
  
  products = Product.objects.filter(seller=request.user.id)
  
  serializer = ProductSerializer(products, many=True)
  return Response(serializer.data)