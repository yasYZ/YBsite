from django.shortcuts import render
from .models import Blog
from django.utils.translation import gettext as _

# Create your views here.


def blog(request, lh):
    current_language = lh

    blogs = Blog.objects.all()

    if current_language == 'Fa':
        return render(request, 'Fa/blog.html', {'blogs': blogs})
    elif current_language == 'fa':
        return render(request, 'Fa/blog.html', {'blogs': blogs})
    else:
        return render(request, 'En/blog.html', {'blogs': blogs})


def blog_detail(request, lh, bi):
    current_language = lh

    blogs = Blog.objects.filter(id=bi)

    if current_language == 'Fa':
        return render(request, 'Fa/blog_detail.html', {'blogs_detail': blogs})
    elif current_language == 'fa':
        return render(request, 'Fa/blog_detail.html', {'blogs_detail': blogs})
    else:
        return render(request, 'En/blog_detail.html', {'blogs_detail': blogs})
