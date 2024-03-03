from django.urls import path
from rest_framework import routers
from .views import sayhello, AssetViewSet,CategoryView

# router = routers.DefaultRouter()
# router.register('assets', AssetViewSet , basename='assets')

urlpatterns = [
    path('', sayhello, name='hello'),
    path('category/',CategoryView.as_view(),name='category')
]