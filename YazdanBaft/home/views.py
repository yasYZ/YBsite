from django.http import HttpResponse
from django.shortcuts import render, redirect
from products.models import Products
from blog.models import Blog
from licences.models import License
from home.models import ContactUS
from .models import gallery, represent
from django.contrib import messages


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
            product_result = Products.objects.filter(name__contains=search_input)
            licences_result = License.objects.filter(title__contains=search_input)
            blog_result = Blog.objects.filter(name__contains=search_input)
            if product_result or licences_result or blog_result is not None:
                return render(request, 'search_result.html', {'blog_result': blog_result, 'product_result': product_result, 'licences_result': licences_result})
            else:
                redirect('/home/')
        else:
            redirect('/home/')


def contact_us(request):
    if request.method == 'POST':
        first_name = request.POST.get('lname')
        last_name = request.POST.get('fname')
        numbers = request.POST.get('num')
        message = request.POST.get('message')
        ContactUS.objects.create(first_name=first_name, last_name=last_name, number=numbers, message=message, is_comment_or_rate=False)
        messages.success(request, 'پیام شما در سیستم ثبت شد از طریق ایمیل یا تلفن با شما ارتباط بر قرار میکنیم!')
        return redirect('contact-us')
    return render(request, 'contact-us.html')


def representatives1(request):
    representatives = represent.objects.all()
    return render(request, 'representatives.html', {'represent': representatives})


def gallerys(request):
    return render(request, 'gallery.html')
