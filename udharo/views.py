from django import views
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Product,Customer
from .forms import ProductForm,CustomerForm

# Create your views here.
# def home(request):
    # p = Product.objects.get(product_name = 'cock')
    # customer = p.total_price()
    # print(customer)
    # c = Customer.objects.get(customer_name ='gori')
    # top to buttom
    # p = c.product_set.all()
    
    # buttom to top
    # c = p.customer.customer_name
    # print(c)
    # for i in p:
        
    #     print(i .product_name)

    # return HttpResponse('helo')
    
# def home(request):
    
#     customer = Customer.objects.all()
#     print(customer)
    
#     return render(request, 'home.html',{"customer" : customer} )

class Home(views.View):
  def get(self, request, *args, **kwargs):
    customer = Customer.objects.all()
    customer_form = CustomerForm()
    
    
    context = {}
    context['customer'] = customer
    context['customer_form'] = customer_form
      
    return render(request, "home.html",context)


  def post(self, request, *args, **kwargs):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        print('form saved')
        form.save()
        return redirect("home")
  
   
      
    return render(request, "home.html",{"message" : "form not submited"})

class Detail(views.View):
  def get(self, request, *args, **kwargs):
    
    id = kwargs['id']
    
    customer = Customer.objects.get(id = id)
    product  = customer.product_set.all()
    
   
    context = {}
    context['products'] = product
    context['cutomer_id'] = customer.id
    
    
      
    return render(request, "detail.html",context)

class Edit(views.View):
  def get(self, request, *args, **kwargs):
    
    id = kwargs['id']
    
    customer = Customer.objects.get(id = id)
    product  = customer.product_set.all()

    context = {}
    context['products'] = product
  
    
      
    return render(request, "detail.html",context)

class Delete(views.View):
  def get(self, request, *args, **kwargs):
    
    id = kwargs['id']
    
    product = Product.objects.get(id = id)
    customer_id = product.customer.id
 
    
    
    context = {}
    context['pid']= id
    context['cid'] = customer_id
    
      
    return render(request, "delete.html",context)
  def post(self, request, *args, **kwargs):
    
    id = kwargs['id']
    
    product = Product.objects.get(id = id)
    customer_id = product.customer.id
    
    
    product.delete()
    
    
      
    return redirect("detail",customer_id)
        
    
    