from rest_framework import serializers

from core.portal.models import Member

class MemberListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'name', 'type', 'status']
        
class MemberWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['name', 'social_media', 'type', 'status', 'biography']
        
class MemberDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'name', 'social_media', 'type', 'status', 'biography']