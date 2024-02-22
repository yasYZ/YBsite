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


def search(request):
    if request.method == 'POST':
        search_input = request.POST.get('search')
        if search_input is not None:
            result = Products.objects.filter(name__contains=search_input)

    return render(request, 'search_result.html')


def contact_us(request):
    return render(request, 'contact-us.html')


def representatives1(request):
    representatives = represent.objects.all()
    return render(request, 'representatives.html', {'represent': representatives})


def gallerys(request):
    return render(request, 'gallery.html')
