from rest_framework import viewsets

from core.portal.models import CourseUser
from core.portal.serializers import CourseUserSerializer

class CourseUserViewSet(viewsets.ModelViewSet):
    queryset = CourseUser.objects.all()
    serializer_class = CourseUserSerializer