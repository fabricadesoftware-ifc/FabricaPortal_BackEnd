from rest_framework import viewsets

from core.portal.models import Area
from core.portal.serializers import AreaSerializer

class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer