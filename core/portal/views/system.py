from rest_framework.viewsets import ModelViewSet
from core.portal.models.system import System
from core.portal.serializers.system import SystemInfoSerializer


class SystemViewSet(ModelViewSet):
    queryset = System.objects.all()
    serializer_class = SystemInfoSerializer
    http_method_names = ['get']

