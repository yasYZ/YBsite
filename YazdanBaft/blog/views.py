from django.shortcuts import render

# Create your views here.


def blog(request):
    return render(request, 'blog.html')


def blog_detail(request):
    return render(request, 'first/blog_detail.html')
