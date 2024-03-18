from django.db.models import Count,Sum
from django.db.models.functions import TruncMonth
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category,Asset,Employee,Distribute
from .serializers import *

class CategoryView(APIView):
   def get(self, request, format=None):
        company_id = request.user.id
        categories = Category.objects.filter(asset__company_id=company_id).all()
        serializer = CategoryAssetCountSerializer(categories, many=True)
        data = {category['name']: category['asset_count'] for category in serializer.data}
        return Response(data)

class AssetViewSet(ModelViewSet):
    def get_queryset(self):
        sort = self.request.GET.get('sort','id')
        company_id = self.request.user.id
        return Asset.objects.filter(company__id=company_id).all().order_by(sort)
        
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetAssetSerializer
        return AssetSerializer
    
class AssetDistributeHistory(APIView):
    def get(self,request,format=None):
        asset_id = request.GET['asset-id']
        queryset = Distribute.objects.filter(asset__id = asset_id)
        serializer = AssetDistHistSerializer(queryset,many=True)
        return  Response(serializer.data)

class EmployeeViewSet(ModelViewSet):
    def get_queryset(self):
        sort = self.request.GET.get('sort','id')
        company_id = self.request.user.id
        return Employee.objects.filter(company__id=company_id).all().order_by(sort)
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetEmployeeSerializer
        return EmployeeSerializer

class UsedAssetHistoryView(APIView):
    def get(self,request,format=None):
        employeeId = request.GET['employeeId']
        queryset = Distribute.objects.filter(employee__id = employeeId)
        serializer = UsedAssetHistorySerializer(queryset,many=True)
        return Response(serializer.data)

class DistributeViewSet(ModelViewSet):
    def get_queryset(self):
        sort = self.request.GET.get('sort','id')
        company_id = self.request.user.id
        return Distribute.objects.filter(company__id=company_id).all().order_by(sort)
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetDistributionSerializer
        return DistributionSerializer

class DashboardView(APIView):
    def get(self,request,format=None):
        company_id = request.user.id

        asset_query = Asset.objects.filter(company_id=company_id)
        employee_query = Employee.objects.filter(company_id=company_id)
        distribute_query = Distribute.objects.filter(company_id=company_id)

        asset_count = asset_query.count()
        employee_count = employee_query.count()
        distributed_asset_count = distribute_query.count()
        asset_price = asset_query.aggregate(total_price = Sum('price'))['total_price']
        employee_salary = employee_query.aggregate(total_salary = Sum('salary'))['total_salary']

        monthly_distribute = distribute_query.annotate(monthly=TruncMonth('provide_date')).values('monthly').annotate(monthly_distribute=Count('id')).values('monthly','monthly_distribute')
        
        distribute_data =  [
            {'month':'January','total_distribute':0},
            {'month':'February','total_distribute':0},
            {'month':'March','total_distribute':0},
            {'month':'April','total_distribute':0},
            {'month':'May','total_distribute':0},
            {'month':'June','total_distribute':0},
            {'month':'July','total_distribute':0},
            {'month':'August','total_distribute':0},
            {'month':'September','total_distribute':0},
            {'month':'October','total_distribute':0},
            {'month':'November','total_distribute':0},
            {'month':'December','total_distribute':0},
        ]
        
        for data in monthly_distribute:
            month = data['monthly'].strftime('%B')
            count = data['monthly_distribute']

            for d in distribute_data:
                if d['month'] == month:
                    d['month'] = month
                    d['total_distribute'] = count

        return Response({
            "asset_count":asset_count,
            "employee_count":employee_count,
            "distributed_asset_count":distributed_asset_count,
            "asset_price" : asset_price,
            "employee_salary":employee_salary,
            "monthly_distribute": distribute_data
        })