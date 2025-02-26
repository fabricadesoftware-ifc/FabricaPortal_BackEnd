from rest_framework import serializers

from core.portal.models import CourseMember

class CourseMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseMember
        fields = ['id', 'member', 'course', 'initial_date', 'final_date']