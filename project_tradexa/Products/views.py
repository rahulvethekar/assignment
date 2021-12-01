from django.shortcuts import redirect, render
from .forms import ProductForm
from .models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def create_product(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_product')

    context = {'form':form}
    template_name = 'product/add_product.html'
    return render(request,template_name,context)

def all_product(request):
    obj = Product.objects.using('Products_db').all()
    context = {'products':obj}
    template_name = 'product/all_product.html'
    return render(request,template_name,context)
def update_product(request,uid):
    obj = Product.objects.using('Products_db').get(id = uid)
    form = ProductForm(instance=obj)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('all_product')

    context = {'form':form}
    template_name = 'product/add_product.html'
    return render(request,template_name,context)    