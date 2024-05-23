from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('blog/', views.blog),
    path('blog/<int:bi>', views.blog_detail),
]