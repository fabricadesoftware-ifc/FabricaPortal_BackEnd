from rest_framework import viewsets

from core.portal.models import Project
from core.portal.serializers import ProjectDetailSerializer, ProjectListSerializer, ProjectWriteSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all() 

    def get_serializer_class(self):
        if self.action == 'list':
            return ProjectListSerializer
        if self.action == 'retrieve':
            return ProjectDetailSerializer
        return ProjectWriteSerializer