from django.db import models
from accounts.models import User



class Article(models.Model):
    title = models.CharField(max_length=100, unique=True)
    abstract = models.TextField(default="")
    url = models.URLField(max_length=1024)
    img_url = models.URLField(max_length=1024, default="")
    section = models.CharField(max_length=30)
    paper = models.CharField(max_length=100)


    def __str__(self):
        return self.title
