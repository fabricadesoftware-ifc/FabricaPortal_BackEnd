from rest_framework import serializers

from core.portal.models.member_tag import MembrerTag

class MemberTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembrerTag
        fields = ['id', 'member', 'tag', 'initial_date', 'final_date']

    def validate(self, value):
        if value['initial_date'] > value['final_date']:
            serializers.ValidationError('A data inicial não pode ser mais recente do que a data final')
        return value