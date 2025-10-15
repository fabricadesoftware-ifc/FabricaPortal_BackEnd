from rest_framework import serializers

from core.portal.models.access import Access

class AccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Access
        fields = "__all__"