from rest_framework import serializers
from core.portal.models.system import System


class SystemInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        fields = ['name', 'version', 'description', 'maintenance_mode']
