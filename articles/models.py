from django.db import models
from accounts.models import User


class Article(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    abstract = models.TextField(default="")
    url = models.URLField(max_length=1024)
    img_url = models.URLField(max_length=1024, default="https://i.guim.co.uk/img/media/29154973f074960f0af69cc6dd7f29cd56de0967/0_50_2016_1210/master/2016.jpg?width=620&dpr=1&s=none")
    section = models.CharField(max_length=30)
    paper = models.CharField(max_length=100)
    published_date = models.CharField(max_length=1024, null=True)
    popularity = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Article_Like(models.Model):
    post = models.ForeignKey(Article, null=True, on_delete=models.CASCADE, related_name='article_like')
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='article_like')
    
    def __str__(self):
        return self.user.username