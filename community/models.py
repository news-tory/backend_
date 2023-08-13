from typing import Collection, Optional
from django.db import models
from accounts.models import User
from articles.models import Article

# 게시글
# 인용한 기사(제목, 이미지)
# 글(누가 썻는지, 프로필 이미지, 좋아요수, 댓글 수, 내용)
# 댓글(누가 썼는지, 프로필 이미지, 좋아요수, 내용)
class Post(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)     # id
    article = models.ForeignKey(Article, null=False, on_delete=models.CASCADE, related_name='article_post_set')  # 기사 id
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='article_post_set')  # 작성자
    created_at = models.DateField(auto_now_add=True)                     # 작성일
    content = models.TextField()                                         # 내용

    def __str__(self):
        return self.content


class Comment(models.Model):
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)  # 게시글 id
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)  # 작성자
    created_at = models.DateField(auto_now_add=True)                     # 작성일
    content = models.TextField()                                         # 내용
    like_cnt = models.IntegerField(default=0)                            # 좋아요 수

    def __str__(self):
        return self.content


class Post_Like(models.Model):
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE, related_name='post_like_set')  # 게시글 번호
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='post_like_set')  # 좋아요 누른 유저
    # related_name을 설정해주면, post.post_like_set.all() 에서처럼 set으로 사용할 수 있음

    def __str__(self):
        return self.user.username