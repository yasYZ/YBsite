from django.shortcuts import render

# Create your views here.


def products(request):
    return render(request, 'products.html')


def products_detail(request, pi):
    return render(request, 'first/product_detail.html')
