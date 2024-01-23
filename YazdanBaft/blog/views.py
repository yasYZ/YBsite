from django.shortcuts import render
from .models import Blog

# Create your views here.


def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})


def blog_detail(request, bi):
    blogs = Blog.objects.filter(id=bi)
    return render(request, 'first/blog_detail.html', {'blogs_detail': blogs})
