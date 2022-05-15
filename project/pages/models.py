from django.db import models


class Videos(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    