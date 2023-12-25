from rest_framework import serializers

from cms.models import InInventory


class InStashSerializer(serializers.ModelSerializer):
    class Meta:
        model = InInventory
        fields = ('id', 'material_name', 'num')
