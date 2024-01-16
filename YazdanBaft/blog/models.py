from django.db import models

# Create your models here.


class Blog(models.Model):
    name = models.CharField(max_length=20)
    discription = models.TextField(max_length=158)
    main_title = models.CharField(max_length=100)
    main_discription = models.TextField(max_length=2500)
    is_None1 = models.BooleanField(default=False)
    title1 = models.CharField(max_length=100)
    discription1 = models.TextField(max_length=2500)
    is_None2 = models.BooleanField(default=False)
    title2 = models.CharField(max_length=100)
    discription2 = models.TextField(max_length=2500)
    is_None3 = models.BooleanField(default=False)
    title3 = models.CharField(max_length=100)
    discription3 = models.TextField(max_length=2500)
    picture = models.ImageField(upload_to='static/image/')

    def __str__(self):
        return self.name    
