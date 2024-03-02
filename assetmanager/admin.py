from django.contrib import admin
from . import models

#-----------Category Admin-------------
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','description']


#-----------Asset Admin-------------
@admin.register(models.Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ['id','name','category','company','buy_date','price']
    list_select_related = ['company']

