from rest_framework import viewsets

from core.portal.models.member_tag import MembrerTag
from core.portal.serializers.member_tag import MemberTagSerializer

class MemberTagViewSet(viewsets.ModelViewSet):
    queryset = MembrerTag.objects.all()
    serializer_class = MemberTagSerializer