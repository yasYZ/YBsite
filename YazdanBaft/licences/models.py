from django.db import models

# Create your models here.


class License(models.Model):
    image = models.ImageField(upload_to='static/images/')
    title = models.CharField(max_length=50)
    caption = models.TextField(max_length=100)
