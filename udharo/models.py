from ast import Import
from statistics import quantiles
from django.db import models
# from django.contrib.auth.models
# Create your models here.



class Customer(models.Model):
    customer_name = models.CharField(max_length=100, blank=False)
    
    
    def __str__(self) -> str:
        return self.customer_name
    
    
    
class  Product(models.Model):
    customer = models.ForeignKey(Customer , on_delete=models.CASCADE, related_name="customerP")
    product_name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.product_name
    
    
    @property
    def total_price(self):
        # print(self.quantity* self.price)
        return self.quantity* self.price
    
    # def total_price(self):
    #     print(self.quantity* self.price)
    #     return self.quantity* self.price
    
    
    
 
    