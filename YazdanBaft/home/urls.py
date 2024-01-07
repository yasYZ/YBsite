from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from . import views
urlpatterns = [
    path('', RedirectView.as_view(url="/home", permanent=True)),
    path('home/', views.home),
]