from rest_framework import viewsets

from core.portal.models import Member
from core.portal.serializers import MemberDetailSerializer, MemberListSerializer, MemberWriteSerializer
from django_filters.rest_framework import DjangoFilterBackend
from core.portal.filters import MemberFilter

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = MemberFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return MemberListSerializer
        if self.action == 'retrieve':
            return MemberDetailSerializer
        return MemberWriteSerializer