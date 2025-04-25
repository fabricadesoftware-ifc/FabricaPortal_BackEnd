from rest_framework import serializers

from core.portal.models import New
from core.uploader.models import Image
from core.uploader.serializers import ImageUploadSerializer

class NewListSerializer(serializers.ModelSerializer):
    image_attachment_key = serializers.SlugRelatedField(
        source="project",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
        many=True
    )
    images = ImageUploadSerializer(required=False, read_only=True, many=True)
    class Meta:
        model = New
        fields = ['id', 'title', 'subject', 'author', 'post_date', 'areas', 'courses','tags', 'members', 'image_attachment_key', 'images']
        
class NewWriteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = New
        fields = ['title', 'subject', 'description', 'author', 'post_date', 'areas', 'courses','tags', 'members', 'images']
        
    def validate(self, value):
        tags = value.get('tags', [])

        if not isinstance(tags, list):
            raise serializers.ValidationError('Tags devem ser uma lista de objetos.')

        for tag in tags:
            if not isinstance(tag, dict) or 'value' not in tag:
                raise serializers.ValidationError('Cada tag deve ser um objeto contendo a chave "value".')

            if not tag['value'].startswith("#"):
                raise serializers.ValidationError('Os valores dos tags devem começar com "#" no início.')
        return value  
        
class NewDetailSerializer(serializers.ModelSerializer):
    images = ImageUploadSerializer(required=False, many=True)
    class Meta:
        model = New
        fields = ['id', 'title', 'subject', 'description', 'author', 'post_date', 'areas', 'courses','tags', 'members', 'images']
