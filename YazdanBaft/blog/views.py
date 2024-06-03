from django.shortcuts import render
from .models import Blog
from django.utils.translation import gettext as _
from home.models import SiteSeoTool

# Create your views here.


def blog(request, lh):
    current_language = lh

    blogs = Blog.objects.all()
    seo_tools = SiteSeoTool.objects.all()

    if current_language == 'Fa':
        return render(request, 'Fa/blog.html', {'blogs': blogs, 'seo': seo_tools})
    elif current_language == 'fa':
        return render(request, 'Fa/blog.html', {'blogs': blogs, 'seo': seo_tools})
    else:
        return render(request, 'En/blog.html', {'blogs': blogs, 'seo': seo_tools})


def blog_detail(request, lh, bi):
    current_language = lh

    blogs = Blog.objects.filter(id=bi)
    seo_tools = SiteSeoTool.objects.all()

    if current_language == 'Fa':
        return render(request, 'Fa/blog_detail.html', {'blogs_detail': blogs, 'seo': seo_tools})
    elif current_language == 'fa':
        return render(request, 'Fa/blog_detail.html', {'blogs_detail': blogs, 'seo': seo_tools})
    else:
        return render(request, 'En/blog_detail.html', {'blogs_detail': blogs, 'seo': seo_tools})
