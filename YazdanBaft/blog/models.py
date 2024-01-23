from django.db import models

# Create your models here.


class Blog(models.Model):
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
    picture = models.ImageField(upload_to='static/images/')

    def __str__(self):
        return self.name    
