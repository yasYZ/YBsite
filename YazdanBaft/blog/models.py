from django.db import models

# Create your models here.


class Blog(models.Model):
    name = models.CharField(max_length=20)
    EN_name = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='static/images/')
    discription = models.TextField(max_length=158)
    EN_discription = models.TextField(max_length=158)

    main_title = models.CharField(max_length=100)
    EN_main_title = models.CharField(max_length=100)
    main_discription = models.TextField(max_length=2500)
    EN_main_discription = models.TextField(max_length=2500)

    title1 = models.CharField(max_length=100, null=True, blank=True)
    EN_title1 = models.CharField(max_length=100, null=True, blank=True)

    left1 = models.BooleanField(default=False, null=True, blank=True)
    right1 = models.BooleanField(default=False, null=True, blank=True)
    picture1 = models.ImageField(upload_to='static/images/', null=True, blank=True)

    discription1 = models.TextField(max_length=2500, null=True, blank=True)
    EN_discription1 = models.TextField(max_length=2500, null=True, blank=True)

    title2 = models.CharField(max_length=100, null=True, blank=True)
    EN_title2 = models.CharField(max_length=100, null=True, blank=True)

    picture2 = models.ImageField(upload_to='static/images/', null=True, blank=True)
    left2 = models.BooleanField(default=False, null=True, blank=True)
    right2 = models.BooleanField(default=False, null=True, blank=True)

    discription2 = models.TextField(max_length=2500, null=True, blank=True)
    EN_discription2 = models.TextField(max_length=2500, null=True, blank=True)

    title3 = models.CharField(max_length=100, null=True, blank=True)
    EN_title3 = models.CharField(max_length=100, null=True, blank=True)

    picture3 = models.ImageField(upload_to='static/images/', null=True, blank=True)
    left3 = models.BooleanField(default=False, null=True, blank=True)
    right3 = models.BooleanField(default=False, null=True, blank=True)

    discription3 = models.TextField(max_length=2500, null=True, blank=True)
    EN_discription3 = models.TextField(max_length=2500, null=True, blank=True)

    title4 = models.CharField(max_length=100, null=True, blank=True)
    EN_title4 = models.CharField(max_length=100, null=True, blank=True)

    picture4 = models.ImageField(upload_to='static/images/', null=True, blank=True)
    left4 = models.BooleanField(default=False, null=True, blank=True)
    right4 = models.BooleanField(default=False, null=True, blank=True)

    discription4 = models.TextField(max_length=2500, null=True, blank=True)
    EN_discription4 = models.TextField(max_length=2500, null=True, blank=True)

    title5 = models.CharField(max_length=100, null=True, blank=True)
    EN_title5 = models.CharField(max_length=100, null=True, blank=True)

    picture5 = models.ImageField(upload_to='static/images/', null=True, blank=True)
    left5 = models.BooleanField(default=False, null=True, blank=True)
    right5 = models.BooleanField(default=False, null=True, blank=True)

    discription5 = models.TextField(max_length=2500, null=True, blank=True)
    EN_discription5 = models.TextField(max_length=2500, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name    
