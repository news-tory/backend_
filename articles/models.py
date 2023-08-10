from django.db import models
from accounts.models import User


# class NYT(models.Model):
#     # id = models.AutoField(primary_key=True, null=False, blank=False)
#     title = models.CharField(max_length=100, unique=True)   # 기사 제목
#     abstract = models.TextField(default="")    # 기사 요약
#     url = models.URLField(max_length=1024)     # 기사 URL
#     img_url = models.URLField(max_length=1024, default="") # 기사 이미지 URL
#     section = models.CharField(max_length=30)  # 기사 태그
#     paper = models.CharField(max_length=100, default="")    # 언론사

#     def __str__(self):
#         return self.title
    

# class Guardian(models.Model):
#     id = models.AutoField(primary_key=True, null=False, blank=False)
#     title = models.CharField(max_length=100, unique=True)   # 기사 제목
#     url = models.URLField(max_length=1024)     # 기사 URL
#     section = models.CharField(max_length=30)  # 기사 태그
#     paper = models.CharField(max_length=100, default="")

#     def __str__(self):
#         return self.title


# class NYT_Comment(models.Model):
#     post = models.ForeignKey(NYT, null=True, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
#     created_at = models.DateField(auto_now_add=True)
#     comment = models.TextField()

#     def __str__(self):
#         return self.comment
    
# class Guardian_Comment(models.Model):
#     post = models.ForeignKey(Guardian, null=True, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
#     created_at = models.DateField(auto_now_add=True)
#     comment = models.TextField()

#     def __str__(self):
#         return self.comment


class Article(models.Model):
    title = models.CharField(max_length=100, unique=True)
    abstract = models.TextField(default="")
    url = models.URLField(max_length=1024)
    img_url = models.URLField(max_length=1024, default="")
    section = models.CharField(max_length=30)
    paper = models.CharField(max_length=100)


    def __str__(self):
        return self.title
