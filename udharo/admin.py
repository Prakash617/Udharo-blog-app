from django.contrib import admin
from .models import Customer,Product

# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_name']
    
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['customer','product_name','quantity','price']
