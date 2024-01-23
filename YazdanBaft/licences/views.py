from django.shortcuts import render
from .models import License

# Create your views here.


def licence(request):
    certificates = License.objects.all()
    return render(request, 'certificates.html', {'licences': certificates})
