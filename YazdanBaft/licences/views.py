from django.shortcuts import render

# Create your views here.


def licence(request):
    return render(request, 'certificates.html')


def licence_detail(request):
    pass
