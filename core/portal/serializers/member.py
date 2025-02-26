from rest_framework import serializers

from core.portal.models import Member

class MemberListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'name', 'type', 'state']
        
class MemberWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['name', 'social_medias', 'type', 'state', 'biography']
        
class MemberDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'name', 'social_medias', 'type', 'state', 'biography']