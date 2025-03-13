from rest_framework import viewsets

from core.portal.models import Project
from core.portal.serializers import ProjectDetailSerializer, ProjectListSerializer, ProjectWriteSerializer
from django_filters.rest_framework import DjangoFilterBackend
from core.portal.filters import ProjectFilter

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all() 
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProjectFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return ProjectListSerializer
        if self.action == 'retrieve':
            return ProjectDetailSerializer
        return ProjectWriteSerializer