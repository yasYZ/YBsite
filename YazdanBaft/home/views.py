from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')


def blog(request):
    return render(request, 'blog.html')


def blog_detail(request, bi):
    return render(request, 'first/blog_detail.html')


def about_us(request):
    return render(request, 'about_us.html')