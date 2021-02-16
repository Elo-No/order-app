from django.db import models

# Create your models here.

class Customers(models.Model):
    Name = models.CharField(max_length=50)
    Family = models.CharField(max_length=50)
    Address = models.TextField()
    Zip_Code = models.CharField(max_length=10)
    Phone = models.CharField(max_length=10)
    Phone_Whats_App = models.CharField(max_length=10)
    Pic= models.ImageField(null=True, blank=True)
    Size_Of_Product = models.CharField(max_length=10)
    Description = models.TextField()
    Debt_Rate = models.FloatField()
    Type_Of_Product = models.CharField(max_length=10)