
from django import forms
from .models import Customer,Product


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
 
        # specify fields to be used
        fields = ["customer_name"]
        
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
 
        # specify fields to be used
        fields = ["customer","product_name","quantity","price"]