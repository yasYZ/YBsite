from django.http import HttpResponse
from django.shortcuts import render
from products.models import Products
from .models import gallery, represent

# Create your views here.


def home(request):
    products = Products.objects.all()
    gallery_img = gallery.objects.all()
    return render(request, 'index.html', {'products': products, 'gallery': gallery_img})


def about_us(request):
    return render(request, 'about_us.html')


def search(request, si):
    return HttpResponse('sdfsdfg')


def contact_us(request):
    return render(request, 'contact-us.html')


def representatives1(request):
    representatives = represent.objects.all()
    return render(request, 'representatives.html', {'represent': representatives})
