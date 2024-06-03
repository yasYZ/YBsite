from django.shortcuts import render
from .models import License
from home.models import SiteSeoTool

# Create your views here.


def licence(request, lh):
    current_language = lh

    certificates = License.objects.all()
    seo = SiteSeoTool.objects.all()

    if current_language == 'fa' or current_language == 'Fa':
        return render(request, 'Fa/certificates.html', {'licences': certificates, 'seo': seo})
    else:
        return render(request, 'En/certificates.html', {'licences': certificates, 'seo': seo})
