from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from YazdanBaft.settings import EMAIL_HOST_USER


# Create your views here.


def email(request):
    user = request.user
    if request.method == 'POST':
        if user.is_staff:
            subject = request.POST.get('subject')
            mail = request.POST.get('email')
            message = request.POST.get('message')
            send_mail(subject=subject, from_email=EMAIL_HOST_USER, recipient_list=mail, fail_silently=False)
    if user.is_staff:
        return render(request, 'email_admin.html')
    else:
        return redirect('/admin')
