from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('certificate/', views.licence),
    path('certificate/<int:ci>', views.licence_detail),
]