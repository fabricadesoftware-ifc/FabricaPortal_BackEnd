from rest_framework import serializers

from core.portal.models import Project
from core.uploader.models import Image
from core.uploader.serializers import ImageUploadSerializer
from core.portal.serializers.member import MemberListSerializer
from core.portal.serializers import AreaSerializer

class ProjectListSerializer(serializers.ModelSerializer):
    image_attachment_key = serializers.SlugRelatedField(
        source="image",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    images = ImageUploadSerializer(required=False, read_only=True, many=True)
    members = MemberListSerializer(many=True, read_only=True)
    technologies = AreaSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = ['id', 'name', 'technologies', 'members', 'state', 'images', 'image_attachment_key', "about"]
        
class ProjectWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'initial_date', 'final_date', 'technologies', 'advisor', 'members', 'state', 'links', 'about', 'images']
        
    def validate(self, value):
        if value['initial_date'] > value['final_date']:
           raise serializers.ValidationError('A value de inicio do projeto não pode ser após o seu término')
        return value                 
        
class ProjectDetailSerializer(serializers.ModelSerializer):
    images = ImageUploadSerializer(required=False, many=True, read_only=True)
    members = MemberListSerializer(many=True, read_only=True)
    technologies = AreaSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = ['id', 'name', 'initial_date', 'final_date', 'technologies', 'advisor', 'members', 'state', 'links', 'about', 'images']
