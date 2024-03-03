from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category,Asset,Employee,Distribute
from .serializers import CategoryAssetCountSerializer,GetAssetSerializer,AssetSerializer,GetEmployeeSerializer,EmployeeSerializer,GetDistributionSerializer,DistributionSerializer


class CategoryView(APIView):
   def get(self, request, format=None):
        company_id = request.user.id
        categories = Category.objects.filter(asset__company_id=company_id).all()
        serializer = CategoryAssetCountSerializer(categories, many=True)
        data = {category['name']: category['asset_count'] for category in serializer.data}
        return Response(data)


class AssetViewSet(ModelViewSet):
    def get_queryset(self):
        company_id = self.request.user.id
        return Asset.objects.filter(company__id=company_id).all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetAssetSerializer
        return AssetSerializer
    

class EmployeeViewSet(ModelViewSet):
    def get_queryset(self):
        company_id = self.request.user.id
        return Employee.objects.filter(company__id=company_id).all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetEmployeeSerializer
        return EmployeeSerializer


class DistributeViewSet(ModelViewSet):
    def get_queryset(self):
        company_id = self.request.user.id
        return Distribute.objects.filter(company__id=company_id).all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetDistributionSerializer
        return DistributionSerializer
