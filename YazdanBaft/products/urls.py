from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('product/', views.products),
    # path('product/<int:pi>/', views.home),
]