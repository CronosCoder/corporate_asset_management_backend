from django.urls import path
from rest_framework import routers
from .views import sayhello, AssetViewSet

# router = routers.DefaultRouter()
# router.register('assets', AssetViewSet , basename='assets')

urlpatterns = [
    path('', sayhello, name='hello'),
]