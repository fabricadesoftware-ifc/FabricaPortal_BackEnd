from rest_framework import serializers
from datetime import date
from core.portal.models.user_tag import UserTag

class EspTagSerializer(serializers.ModelSerializer):
    valid = serializers.SerializerMethodField()

    class Meta:
        model = UserTag
        fields = ['tag','valid']
    
    def get_valid(self, obj):
        today = date.today()
        user = obj.user
        status = user.status
        if obj.initial_date <= today <= obj.final_date and status == "Ativo":
            return True
        else:
            return False