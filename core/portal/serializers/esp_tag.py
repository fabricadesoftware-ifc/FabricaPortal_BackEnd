from rest_framework import serializers
from datetime import datetime
from core.portal.models.user_tag import UserTag

class EspTagSerializer(serializers.ModelSerializer):
    valid = serializers.SerializerMethodField()

    class Meta:
        model = UserTag
        fields = ['tag','valid']
    
    def get_valid(self, obj):
        today = datetime.now().date()
        user = obj.user
        type = user.type
        if obj.initial_date <= today <= obj.final_date and type == "ATIVO":
            return True
        else:
            return False