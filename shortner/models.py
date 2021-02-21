from django.db import models

class GeneratedLinks(models.Model):
    short_link = models.CharField(max_length=300,default="gg",unique=True)
    full_link = models.CharField(max_length=1000,unique=True)

