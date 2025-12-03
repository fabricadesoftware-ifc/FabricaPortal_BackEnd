from rest_framework import generics
from core.portal.models import UserTag
from core.portal.serializers import EspTagSerializer
from django_project.permission import EspTagPermission

class EspTagListAPIView(generics.ListAPIView):
    permission_classes = [EspTagPermission]
    queryset = UserTag.objects.all()
    serializer_class = EspTagSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)