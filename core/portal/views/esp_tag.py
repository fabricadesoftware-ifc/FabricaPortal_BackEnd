from rest_framework import generics
from core.portal.models import UserTag
from core.portal.serializers import EspTagSerializer

class EspTagListAPIView(generics.ListAPIView):
    queryset = UserTag.objects.all()
    serializer_class = EspTagSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)