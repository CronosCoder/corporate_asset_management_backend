from .models import *
from rest_framework import serializers
from authentication.models import Company

class CategoryAssetCountSerializer(serializers.ModelSerializer):
    asset_count = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['name', 'asset_count']

    def get_asset_count(self, obj):
        return obj.asset.count()

class CategoryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class CompanyNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name']


''' Asset Serializer'''

class GetAssetSerializer(serializers.ModelSerializer):
    category = CategoryNameSerializer(read_only=True)
    company = CompanyNameSerializer(read_only=True)
    class Meta:
        model = Asset
        fields = ['id','name','description','price','buy_date','warranty','category','company']

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['id','name','description','price','buy_date','warranty','category','company']