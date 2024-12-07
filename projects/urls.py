from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, basename='projects')

urlpatterns = router.urls
# aqui se generan las distintas peticiones HTTP
