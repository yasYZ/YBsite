from django.db import models

# Create your models here.


class represent(models.Model):
    title = models.CharField(max_length=35)
    name = models.CharField(max_length=35)
    address = models.TextField(max_length=110)
    phone = models.CharField(max_length=11)
    image = models.ImageField(upload_to='static/images/')

    def __str__(self):
        return self.title


class gallery(models.Model):
    file = models.FileField(upload_to='static/gallery/')
