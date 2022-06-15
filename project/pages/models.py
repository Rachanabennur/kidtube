from statistics import mode
from django.db import models


    
class Feed(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    vid = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default="")
    tags = models.BooleanField(default=False)
    url = models.URLField(default="")
    comments = models.CharField(max_length=1000, default="")    

class CommentClass(models.Model):
    video_id = models.CharField(max_length=5)
    message = models.CharField(max_length=200)