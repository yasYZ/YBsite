from django.http import HttpResponse
from django.shortcuts import render, redirect
from products.models import Products
from blog.models import Blog
from licences.models import License
from home.models import ContactUS
from .models import gallery, represent, SiteSeoTool, Colleagues
from django.contrib import messages
from django.utils.translation import get_language
from django.views.generic import ListView

# Create your views here.


class MyListView(ListView):
    model = SiteSeoTool

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seo'] = self.model
        return context


def set_language(request, **args):
    current_language = get_language()

    if not args:
        if current_language == 'fa':
            return redirect('fa/')
        else:
            return redirect('en/')
    else:
        return render(request, '404.html', status=404)


def home(request, lh):
    products = Products.objects.all()
    gallery_img = gallery.objects.all()
    col = Colleagues.objects.all()


    current_language = lh
    if current_language == 'fa':
        return render(request, 'Fa/index.html', {'products': products, 'gallery': gallery_img, 'col': col})
    elif current_language == 'Fa':
        return render(request, 'Fa/index.html', {'products': products, 'gallery': gallery_img, 'col': col})
    else:
        return render(request, 'En/index.html', {'products': products, 'gallery': gallery_img, 'col': col})


def about_us(request, lh):
    current_language = lh

    if current_language == 'fa':
        return render(request, 'Fa/about_us.html')
    elif current_language == 'Fa':
        return render(request, 'Fa/about_us.html')
    else:
        return render(request, 'En/about_us.html')


def search(request, lh):
    current_language = lh

    if request.method == 'POST':
        search_input = request.POST.get('search')
        if search_input:
            product_result = Products.objects.filter(name__contains=search_input)
            en_product_result = Products.objects.filter(EN_name__contains=search_input)
            licences_result = License.objects.filter(title__contains=search_input)
            en_licences_result = License.objects.filter(EN_title__contains=search_input)
            blog_result = Blog.objects.filter(name__contains=search_input)
            en_blog_result = Blog.objects.filter(EN_name__contains=search_input)
            if product_result or licences_result or blog_result or en_blog_result or en_licences_result or en_product_result:
                if current_language == 'Fa':
                    return render(request, 'Fa/search_result.html', {'blog_result': blog_result if blog_result else en_blog_result,
                                                                     'product_result': product_result if product_result else en_product_result,
                                                                     'licences_result': licences_result if licences_result else en_licences_result})
                elif current_language == 'fa':
                    return render(request, 'Fa/search_result.html', {'blog_result': blog_result if blog_result else en_blog_result,
                                                                     'product_result': product_result if product_result else en_product_result,
                                                                     'licences_result': licences_result if licences_result else en_licences_result})
                else:
                    return render(request, 'En/search_result.html', {'blog_result': en_blog_result if en_blog_result else blog_result,
                                                                     'product_result': en_product_result if en_product_result else product_result,
                                                                     'licences_result': en_licences_result if en_licences_result else licences_result})
            else:
                if current_language == 'Fa':
                    messages.error(request, 'نتیجه ای یافت نشد')
                    return redirect('/Fa/home/')
                elif current_language == 'fa':
                    messages.error(request, 'نتیجه ای یافت نشد')
                    return redirect('/fa/home/')
                else:
                    messages.error(request, 'Not Found!')
                    return redirect('/en/home/')
        else:
            if current_language == 'Fa':
                messages.error(request, 'لطفا چیزی وارد نمایید')
                return redirect('/Fa/home/')
            elif current_language == 'fa':
                messages.error(request, 'لطفا چیزی وارد نمایید')
                return redirect('/fa/home/')
            else:
                messages.error(request, 'please fill the fields')
                return redirect('/en/home/')
    else:
        return render(request, '404.html')


def contact_us(request, lh):
    current_language = lh

    if request.method == 'POST':
        first_name = request.POST.get('lname')
        last_name = request.POST.get('fname')
        numbers = request.POST.get('num')
        message = request.POST.get('message')
        ContactUS.objects.create(first_name=first_name, last_name=last_name, number=numbers, message=message, is_comment_or_rate=False)

        if current_language == 'Fa':
            messages.success(request, 'پیام شما در سیستم ثبت شد از طریق ایمیل یا تلفن با شما ارتباط بر قرار میکنیم!')
            return redirect('/fa')
        elif current_language == 'fa':
            messages.success(request, 'پیام شما در سیستم ثبت شد از طریق ایمیل یا تلفن با شما ارتباط بر قرار میکنیم!')
            return redirect('/fa')
        else:
            messages.success(request, 'Your message is successfully sent!')
            return redirect('/en')

    if current_language == 'Fa':
        return render(request, 'Fa/contact-us.html')
    elif current_language == 'fa':
        return render(request, 'Fa/contact-us.html')
    else:
        return render(request, 'En/contact-us.html')


def representatives1(request, lh):
    current_language = lh

    representatives = represent.objects.all()

    if current_language == 'Fa':
        return render(request, 'Fa/representatives.html', {'represent': representatives})
    elif current_language == 'fa':
        return render(request, 'Fa/representatives.html', {'represent': representatives})
    else:
        return render(request, 'En/representatives.html', {'represent': representatives})


def custom_404(request, exception):
    return render(request, '404.html', status=404)
