from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']


class Asset(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField()
    buy_date = models.DateField()
    warranty = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='asset')
    company = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='asset')

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class Employee(models.Model):
    name = models.CharField(max_length=255)
    designation  = models.CharField(max_length=255)  
    description = models.TextField()
    salary = models.PositiveIntegerField()
    join_date = models.DateField()
    company = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='employee',default=None)

    def __str__(self) -> str:
        return f'{self.name}'
    

class Distribute(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE,related_name='distribute')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,related_name='distribute')
    provide_conditions = models.TextField()
    return_conditions = models.TextField()
    provide_date = models.DateField()
    return_date = models.DateField()
    company = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='distribute',default=None)


