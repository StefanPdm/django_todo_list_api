from django.shortcuts import render
from rest_framework import routers, serializers, viewsets, permissions
from . models import *

from . serializers import *

# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    # API endpoint that allows users to be viewed or edited.
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer
    permission_classes = [] # alternativ [permissions.IsAuthenticated]
    
class KonnektorViewSet(viewsets.ModelViewSet):
    # API endpoint that allows users to be viewed or edited.
    queryset = Konnektor.objects.all()
    serializer_class = KonnektorSerializer
    permission_classes = [] # alternativ [permissions.IsAuthenticated]