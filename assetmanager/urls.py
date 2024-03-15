from django.urls import path,include
from rest_framework import routers
from .views import AssetViewSet,CategoryView,EmployeeViewSet,DistributeViewSet,DashboardView,AssetDistributeHistory

router = routers.DefaultRouter()
router.register('assets', AssetViewSet , basename='assets')
router.register('employee', EmployeeViewSet , basename='employees')
router.register('distribute', DistributeViewSet , basename='distribute')

urlpatterns = [
    path('category/',CategoryView.as_view(),name='category'),
    path('dashboard/',DashboardView.as_view(),name='dashboard'),
    path('asset-distribution-history/',AssetDistributeHistory.as_view(),name="asset_dist-hist"),
    path('',include(router.urls)),
]