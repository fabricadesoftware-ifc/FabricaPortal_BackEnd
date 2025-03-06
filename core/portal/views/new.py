from rest_framework import viewsets

from core.portal.models import New
from core.portal.serializers import NewDetailSerializer, NewListSerializer, NewWriteSerializer

class NewViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return NewListSerializer
        if self.action == 'retrieve':
            return NewDetailSerializer
        return NewWriteSerializer