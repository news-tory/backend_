from django.db import models
from accounts.models import User


class Article(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    abstract = models.TextField(default="")
    url = models.URLField(max_length=1024)
    img_url = models.URLField(max_length=1024, default="")
    section = models.CharField(max_length=30)
    paper = models.CharField(max_length=100)
    published_date = models.CharField(max_length=1024, null=True)

    def __str__(self):
        return self.title


class Article_Like(models.Model):
    post = models.ForeignKey(Article, null=True, on_delete=models.CASCADE, related_name='article_like')
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='article_like')
    
    def __str__(self):
        return self.user.username