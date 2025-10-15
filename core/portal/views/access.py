from rest_framework import viewsets

from core.portal.models.access import Access
from core.portal.serializers.access import AccessSerializer

class AccessViewSet(viewsets.ModelViewSet):
    queryset = Access.objects.all()
    serializer_class = AccessSerializer