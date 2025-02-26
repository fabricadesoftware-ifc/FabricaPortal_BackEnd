from rest_framework import viewsets

from core.portal.models import CourseMember
from core.portal.serializers import CourseMemberSerializer

class CourseMemberViewSet(viewsets.ModelViewSet):
    queryset = CourseMember.objects.all()
    serializer_class = CourseMemberSerializer