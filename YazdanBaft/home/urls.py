from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url="/home", permanent=True)),
    path('home/', views.home),
    path('about-us/', views.about_us),
    path('search/', views.search, name='search'),
    path('contact-us/', views.contact_us, name='contact-us'),
]
