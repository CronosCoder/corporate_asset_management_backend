from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet

# Create your views here.

def sayhello(request):
   return HttpResponse('Hello, world')

class AssetViewSet(ModelViewSet):
    pass

