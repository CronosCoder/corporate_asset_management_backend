from .models import *
from datetime import date
from rest_framework import serializers
from authentication.models import Company

'''Company Serializer'''
class CompanyNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id','name']

'''Category Serializer'''
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
        fields = ['id','name']

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

class SimpleAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['id','name']

'''Employee Serializer'''
class GetEmployeeSerializer(serializers.ModelSerializer):
    company = CompanyNameSerializer(read_only=True)
    class Meta:
        model = Employee
        fields = ['id','name','designation','description','salary','join_date','company']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','name','designation','description','salary','join_date','company']

class SimpleEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','name']

'''Distribution Serializer'''
class DistributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distribute
        fields = ['asset','employee','provide_conditions','return_conditions','provide_date','return_date','company','returned']

class GetDistributionSerializer(serializers.ModelSerializer):
    asset = SimpleAssetSerializer(read_only=True)
    employee = SimpleEmployeeSerializer(read_only=True)
    company = CompanyNameSerializer(read_only=True)
    status = serializers.SerializerMethodField()

    def get_status(self,distribute:Distribute):
        if  distribute.returned :
            return 'Free'
        else:
            current_day = date.today()
            if distribute.return_date < current_day:
                return 'Due to return'
            else:
                return 'Using'

    class Meta:
        model = Distribute
        fields = ['id','asset','employee','provide_conditions','return_conditions','provide_date','return_date','company','status','returned']

class AssetDistHistSerializer(serializers.ModelSerializer):
    employee = SimpleEmployeeSerializer(read_only=True)
    class Meta:
        model = Distribute
        fields = ['id','employee','provide_conditions','return_conditions','return_date','returned']

class UsedAssetHistorySerializer(serializers.ModelSerializer):
    asset = SimpleAssetSerializer(read_only=True)
    class Meta:
        model = Distribute
        fields = ['id','asset','provide_conditions','return_conditions','return_date','returned']