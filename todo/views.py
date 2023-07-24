from django.shortcuts import render
from rest_framework import routers, serializers, viewsets, permissions
from . models import *

from . serializers import TodoSerializer

# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    # API endpoint that allows users to be viewed or edited.
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer
    permission_classes = [] # alternativ [permissions.IsAuthenticated]