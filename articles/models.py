from django.db import models
from accounts.models import User



class Article(models.Model):
    title = models.CharField(max_length=100, unique=True)
    abstract = models.TextField(default="")
    url = models.URLField(max_length=1024)
    img_url = models.URLField(max_length=1024, default="https://i.guim.co.uk/img/media/29154973f074960f0af69cc6dd7f29cd56de0967/0_50_2016_1210/master/2016.jpg?width=620&dpr=1&s=none")
    section = models.CharField(max_length=30)
    paper = models.CharField(max_length=100)


    def __str__(self):
        return self.title
