from django.shortcuts import render
from .models import Products

# Create your views here.


def products(request):
    product = Products.objects.all()
    return render(request, 'products.html', {'products': product})


def products_detail(request, pi):
    product = Products.objects.filter(id=pi)
    return render(request, 'first/product_detail.html', {'product': product})
