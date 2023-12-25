from rest_framework import serializers

from cms.models import OutInventory


class OutStashSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutInventory
        fields = ('material', 'num')
