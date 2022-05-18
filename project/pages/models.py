from distutils.command.upload import upload
from django.db import models
    
class Feed(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    vid = models.CharField(max_length=100)
    tag = models.BooleanField(default=False)
    category = models.CharField(max_length=100)
    url = models.URLField(default="")
    comments = models.CharField(max_length=1000, default="")


    
    