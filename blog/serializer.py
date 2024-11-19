from rest_framework import serializers
from .models import Blog
from django.contrib.auth.models import User

class BlogSerializers(serializers.ModelSerializer):
  class Meta:
    model = Blog
    fields = ('__all__') 


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields =['id', 'username', 'password', 'email']
    extra_kwargs = {
      "email":{'required':True}
    }