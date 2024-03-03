from django.urls import path,include
from rest_framework import routers
from .views import AssetViewSet,CategoryView,EmployeeViewSet,DistributeViewSet

router = routers.DefaultRouter()
router.register('assets', AssetViewSet , basename='assets')
router.register('employee', EmployeeViewSet , basename='employees')
router.register('distribute', DistributeViewSet , basename='distribute')

urlpatterns = [
    path('category/',CategoryView.as_view(),name='category'),
    path('',include(router.urls))
]