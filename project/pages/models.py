from distutils.command.upload import upload
from django.db import models


class Videos(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    
class Feed(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    long_desc = models.CharField(max_length=200)
    img = models.ImageField(upload_to='images/')
    vid = models.FileField(upload_to='videos/')


    
    