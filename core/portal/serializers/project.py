from rest_framework import serializers

from core.portal.models import Project
from core.uploader.models import Image
from core.uploader.serializers import ImageUploadSerializer

class ProjectListSerializer(serializers.ModelSerializer):
    image_attachment_key = serializers.SlugRelatedField(
        source="image",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    image = ImageUploadSerializer(required=False, read_only=True)
    class Meta:
        model = Project
        fields = ['id', 'name', 'areas', 'members', 'state', 'image', 'image_attachment_key']
        
class ProjectWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'initial_date', 'final_date', 'areas', 'advisor', 'members', 'state', 'links', 'about', 'image']
        
    def validate(self, value):
        if value['initial_date'] > value['final_date']:
           raise serializers.ValidationError('A value de inicio do projeto não pode ser após o seu término')
        return value                 
        
class ProjectDetailSerializer(serializers.ModelSerializer):
    image = ImageUploadSerializer(required=False)
    class Meta:
        model = Project
        fields = ['id', 'name', 'initial_date', 'final_date', 'areas', 'advisor', 'members', 'state', 'links', 'about', 'image']
