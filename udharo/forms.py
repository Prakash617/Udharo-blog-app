
from django import forms
from .models import Customer,Product


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
 
        # specify fields to be used
        fields = ["customer_name"]
        
class ProductsForm(forms.ModelForm):
    class Meta:
        model = Product
        # customer = forms.ModelChoiceField(Customer.objects.all())
        # specify fields to be used
        fields = ["customer","product_name","quantity","price"]
        # widgets = {
        #     'customer': forms.HiddenInput(),
        # }
        
        # def clean_nameofdata(self):
        #     data = self.cleaned_data['customer']
            # do some stuff
            # return data
        
        
class ProductForm(forms.ModelForm):
    class Meta:
        
        model = Product
 
        fields = ["product_name","quantity","price"]
        # widgets = {
        #     'customer': forms.HiddenInput(),
        # }
        # def save(self, commit=True):
        #     instance = super().save(commit)
        #     # set Car reverse foreign key from the Person model
        #     instance.car_set.add(self.cleaned_data['customer'])
        #     return instance 
        
        # def clean_field(self):
        #     data = self.cleaned_data.get("product_name")
            
        #     return data
        
        
        