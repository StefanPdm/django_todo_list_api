
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from todo.views import *

router = routers.DefaultRouter()
router.register(r'todos', TodoViewSet)
router.register(r'konnektors', KonnektorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
   
    
]
