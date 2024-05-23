from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from YazdanBaft.settings import EMAIL_HOST_USER
from django.contrib import messages


# Create your views here.


def email(request, lh):
    user = request.user
    if request.method == 'POST':
        if user.is_staff:
            subject = str(request.POST.get('subject'))
            mail = str(request.POST.get('email'))
            message = str(request.POST.get('message'))
            if message and subject and mail is not None:
                send_mail(subject=subject, message=message, from_email=EMAIL_HOST_USER, recipient_list=[mail], fail_silently=False)
                messages.success(request, 'پیام ارسال شد!')
            else:
                messages.error(request, 'چیزی رو اشتباه وارد کردید برای اطمینان دوباره جاهای خالی را پر کنید!')
    if user.is_staff:
        return render(request, 'Fa/email_admin.html')
    else:
        return redirect('/admin')
