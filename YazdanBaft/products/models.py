from django.db import models

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Products(models.Model):
    name = models.CharField(max_length=20)
    discription = models.TextField(max_length=158)
    main_title = models.CharField(max_length=100)
    main_discription = models.TextField(max_length=2500)
    title1 = models.CharField(max_length=100, null=True, blank=True)
    discription1 = models.TextField(max_length=2500, null=True, blank=True)
    title2 = models.CharField(max_length=100, null=True, blank=True)
    discription2 = models.TextField(max_length=2500, null=True, blank=True)
    title3 = models.CharField(max_length=100, null=True, blank=True)
    discription3 = models.TextField(max_length=2500, null=True, blank=True)
    title4 = models.CharField(max_length=100, null=True, blank=True)
    discription4 = models.TextField(max_length=2500, null=True, blank=True)
    title5 = models.CharField(max_length=100, null=True, blank=True)
    discription5 = models.TextField(max_length=2500, null=True, blank=True)
    is_special = models.BooleanField(default=False)
    is_main_page = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='static/images/')

    def __str__(self):
        return self.name    
