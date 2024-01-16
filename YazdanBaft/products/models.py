from django.db import models

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Products(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=158)
    price = models.DecimalField(default=0, max_digits=50, decimal_places=0)
    is_special = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='static/image/')

    def __str__(self):
        return self.name    
