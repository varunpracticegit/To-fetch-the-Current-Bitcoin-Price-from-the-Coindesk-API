from django.db import models

# Create your models here.
class Category(models.Model):
    categoryname = models.CharField(max_length=70)

class Products(models.Model):
    categoryname  = models.ForeignKey('Category', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=70)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    description = models.TextField(max_length=100)
