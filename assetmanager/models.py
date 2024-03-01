from django.db import models
from authentication.models import Company


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Asset(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company')
    price = models.DecimalField(max_digits=4, decimal_places=2)
    buy_date = models.DateTimeField(auto_now_add=True)
    warranty = models.DateField()

class Employee(models.Model):
    name = models.CharField(max_length=255)
    designation  = models.CharField(max_length=255)  
    description = models.TextField()
    salary = models.PositiveIntegerField()
    join_date = models.DateField()

    def __str__(self) -> str:
        return f'{self.name}'
    

class Distribute(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    provide_conditions = models.TextField()
    return_conditions = models.TextField()
    provide_date = models.DateField()
    return_date = models.DateField()


