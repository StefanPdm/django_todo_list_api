from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from . models import *

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'completed', 'user']
        
class KonnektorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Konnektor
        fields = ['k_id', 'k_name', 'k_is_active', 'k_online_since', 'k_firmware_version', 'k_update_available']