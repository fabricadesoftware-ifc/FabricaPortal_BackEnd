from rest_framework import serializers

from core.portal.models import Member
from core.uploader.models import Image
from core.uploader.serializers import ImageUploadSerializer

class MemberListSerializer(serializers.ModelSerializer):
    image_attachment_key = serializers.SlugRelatedField(
        source="project",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    image = ImageUploadSerializer(required=False, read_only=True)
    class Meta:
        model = Member
        fields = ['id', 'name', 'type', 'status', 'image_attachment_key', 'image', 'biography']
        
class MemberWriteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Member
        fields = ['name', 'social_media', 'type', 'status', 'biography', 'image']
        
class MemberDetailSerializer(serializers.ModelSerializer):
    image = ImageUploadSerializer(required=False)
    class Meta:
        model = Member
        fields = ['id', 'name', 'social_media', 'type', 'status', 'biography', 'image']