from django.urls import path,include
from rest_framework import routers
from .views import AssetViewSet,CategoryView

router = routers.DefaultRouter()
router.register('assets', AssetViewSet , basename='assets')

urlpatterns = [
    path('category/',CategoryView.as_view(),name='category'),
    path('',include(router.urls))
]