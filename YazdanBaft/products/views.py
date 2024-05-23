from django.shortcuts import render
from .models import Products

# Create your views here.


def products(request, lh):
    current_language = lh

    product = Products.objects.all()

    if current_language == 'fa' or current_language == 'Fa':
        return render(request, 'Fa/products.html', {'products': product})
    else:
        return render(request, 'En/products.html', {'products': product})


def products_detail(request, lh, pi):
    current_language = lh

    product = Products.objects.filter(id=pi)

    if current_language == 'fa' or current_language == 'Fa':
        return render(request, 'Fa/product_detail.html', {'product': product})
    else:
        return render(request, 'En/product_detail.html', {'product': product})
