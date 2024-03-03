from .models import *
from rest_framework import serializers

class CategoryAssetCountSerializer(serializers.ModelSerializer):
    asset_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['name', 'asset_count']

    def get_asset_count(self, obj):
        return obj.asset.count()