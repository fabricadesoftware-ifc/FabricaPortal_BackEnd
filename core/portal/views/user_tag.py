from rest_framework import viewsets

from core.portal.models.user_tag import UserTag
from core.portal.serializers.user_tag import UserTagSerializer

class UserTagViewSet(viewsets.ModelViewSet):
    queryset = UserTag.objects.all()
    serializer_class = UserTagSerializer