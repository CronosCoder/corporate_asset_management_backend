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

#----------Employee Admin-------------
@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','name','designation','company','salary']
    list_select_related = ['company']


#----------Distribute Admin------------
@admin.register(models.Distribute)
class DistributeAdmin(admin.ModelAdmin):
    list_display = ['asset','employee','company','returned','provide_date','return_date']
    list_select_related = ['asset','employee','company']
