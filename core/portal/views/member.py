from rest_framework import viewsets

from core.portal.models import Member
from core.portal.serializers import MemberDetailSerializer, MemberListSerializer, MemberWriteSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return MemberListSerializer
        if self.action == 'retrieve':
            return MemberDetailSerializer
        return MemberWriteSerializer