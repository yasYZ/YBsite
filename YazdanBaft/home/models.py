from django.db import models

# Create your models here.


class represent(models.Model):
    title = models.CharField(max_length=35)
    EN_title = models.CharField(max_length=35)
    name = models.CharField(max_length=35)
    EN_name = models.CharField(max_length=35)
    address = models.TextField(max_length=110)
    EN_address = models.TextField(max_length=110)
    phone = models.CharField(max_length=11)
    image = models.ImageField(upload_to='static/images/')

    def __str__(self):
        return self.title


class gallery(models.Model):
    file = models.FileField(upload_to='static/gallery/')
    is_image = models.BooleanField(default=False)
    is_Video = models.BooleanField(default=False)


class ContactUS(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    number = models.CharField(max_length=11)
    message = models.TextField(max_length=500)
    is_comment_or_rate = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name


class Colleagues(models.Model):
    image = models.ImageField(upload_to='static/gallery/')
    name = models.CharField(max_length=35)


class SiteSeoTool(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    EN_title = models.CharField(max_length=200)
    EN_description = models.TextField(max_length=500)
    keywords = models.TextField(max_length=500, blank=True)
    EN_keywords = models.TextField(max_length=500, blank=True)
    Fa_Href_Lang = models.CharField(max_length=200, blank=True)
    Fa_Href_Lang_Url = models.CharField(max_length=200, blank=True)
    EN_Href_Lang = models.CharField(max_length=200, blank=True)
    EN_Href_Lang_Url = models.CharField(max_length=200, blank=True)
