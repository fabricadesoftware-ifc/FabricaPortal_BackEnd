from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from core.authentication.models import User
from core.uploader.models import Image
from core.uploader.serializers import ImageUploadSerializer

class UserWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'linkedin', 'github', 'instagram', 'type', 'status', 'biography', 'image', 'date_joined', 'last_login']
        read_only_fields = ['id', 'date_joined', 'last_login', 'date_joined']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este email já está em uso")
        return value

    def validate_username(self, value):
        if User.objects.filter(name=value).exists():
            raise serializers.ValidationError("Este nome de usuário já está em uso")
        if len(value) < 3:
            raise serializers.ValidationError("Nome de usuário deve ter pelo menos 3 caracteres")
        return value

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Nome deve ter pelo menos 3 caracteres")
        return value

class UserListSerializer(serializers.ModelSerializer):
    image_attachment_key = serializers.SlugRelatedField(
        source="project",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    image = ImageUploadSerializer(required=False, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'name', 'type', 'status', 'image_attachment_key', 'image', 'biography', 'linkedin', 'github', 'instagram']

class UserDetailSerializer(serializers.ModelSerializer):
    image = ImageUploadSerializer(required=False)
    class Meta:
        model = User
        fields = ['id', 'name', 'type', 'status', 'biography', 'image', 'linkedin', 'github', 'instagram']

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        
        data['id'] = self.user.id
        data['name'] = self.user.name
        data['email'] = self.user.email

        
        return data