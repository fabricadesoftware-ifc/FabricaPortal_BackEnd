from rest_framework import viewsets

from core.portal.models import Tag
from core.portal.serializers import TagSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer