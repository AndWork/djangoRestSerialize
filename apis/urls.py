from django.urls import include, path
from rest_framework import routers

from .views import *

#definir router
router = routers.DefaultRouter()
#definir caminho do router e seu ViewSet(de views)
router.register(r'geeks', GeeksViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]