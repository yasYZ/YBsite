from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.represent)
admin.site.register(models.gallery)

admin.site.site_header = 'Yazdan Baft Default Panel'
admin.site.site_title = 'Yazdan Baft'
