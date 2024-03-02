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
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    company = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='company')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']


class Employee(models.Model):
    name = models.CharField(max_length=255)
    designation  = models.CharField(max_length=255)  
    description = models.TextField()
    salary = models.PositiveIntegerField()
    join_date = models.DateField()

    def __str__(self) -> str:
        return f'{self.name}'
    

class Distriute(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    provide_conditions = models.TextField()
    return_conditions = models.TextField()
    provide_date = models.DateField()
    return_date = models.DateField()


