from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def home(request):
    products = Product.objects.order_by('-registeredDateTime')
    return render(request, 'home.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product':product})