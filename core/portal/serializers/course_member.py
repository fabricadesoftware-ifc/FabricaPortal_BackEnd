from rest_framework import serializers

from core.portal.models import CourseMember

class CourseMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseMember
        fields = ['id', 'member', 'course', 'initial_year', 'final_year']
        
    def validate(self, value):
        if value['initial_year'] > value['final_year']:
            raise serializers.ValidationError('O ano de ingresso não pode ser após o egresso')
        return value
        
    def validate_year(self, value):
        if value['initial_year'] < 2000:
            return serializers.ValidationError('O ano é inválido')
        return value
