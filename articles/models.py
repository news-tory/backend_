from django.db import models

class Article(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    title = models.CharField(max_length=100)   # 기사 제목
    abstract = models.TextField(default="")    # 기사 요약
    url = models.URLField(max_length=1024)     # 기사 URL
    img_url = models.URLField(max_length=1024, default="") # 기사 이미지 URL
    section = models.CharField(max_length=30)  # 기사 태그
    # date = models.CharField(max_length=30)
    paper = models.CharField(max_length=100, default="")    # 언론사

    def __str__(self):
        return self.title