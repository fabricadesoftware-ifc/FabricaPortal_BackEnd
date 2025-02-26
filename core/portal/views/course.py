from rest_framework import viewsets

from core.portal.models import Course
from core.portal.serializers import CourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer