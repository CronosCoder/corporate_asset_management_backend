from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category,Asset
from .serializers import CategoryAssetCountSerializer,GetAssetSerializer,AssetSerializer


class CategoryView(APIView):
   def get(self, request, format=None):
        company_id = request.GET.get('company_id')
        categories = Category.objects.filter(asset__company_id=company_id).distinct()
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
