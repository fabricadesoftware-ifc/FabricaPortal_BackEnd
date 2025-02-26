from rest_framework import serializers

from core.portal.models import Project

class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'areas', 'members', 'state']
        
class ProjectWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'initial_date', 'final_date', 'areas', 'advisor', 'members', 'state', 'deploy_link', 'front_repo_link', 'back_repo_link', 'design_link', 'about']
        
class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'initial_date', 'final_date', 'areas', 'advisor', 'members', 'state', 'deploy_link', 'front_repo_link', 'back_repo_link', 'design_link', 'about']
