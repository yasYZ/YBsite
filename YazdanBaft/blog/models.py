from django.db import models

# Create your models here.


class blog_detail_name(models.Model):
    title = models.CharField(max_length=100)
    title_caption = models.TextField(max_length=500)
    name1 = models.CharField(max_length=100)
    discription1 = models.TextField(max_length=500)
    
    def __str__(self):
        return self.title   


class Blog(models.Model):
    name = models.CharField(max_length=20)
    discription = models.TextField(max_length=158)
    details = models.ForeignKey(blog_detail_name, on_delete=models.CASCADE, default=1)
    price = models.DecimalField(default=0, max_digits=50, decimal_places=0)
    is_special = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='static/image/')

    def __str__(self):
        return self.name    
