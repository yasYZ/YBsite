from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.represent)
admin.site.register(models.gallery)
admin.site.register(models.ContactUS)
admin.site.register(models.SiteSeoTool)
admin.site.register(models.Colleagues)

admin.site.site_header = 'Yazdan Baft Default Panel'
admin.site.site_title = 'Yazdan Baft'
