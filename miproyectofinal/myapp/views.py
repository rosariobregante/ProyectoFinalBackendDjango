from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Customer
from .forms import ProductForm, CustomerForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'myapp/product_list.html', {'products': products})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'myapp/product_form.html', {'form': form})

def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'myapp/product_form.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required
def restricted_view(request):
    # Solo los usuarios logueados pueden acceder
    return render(request, 'myapp/restricted.html')

from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    from django.shortcuts import render

def home(request):
    return render(request, 'home.html')