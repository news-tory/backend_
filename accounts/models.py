from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

class CustomUser(AbstractUser): # 장고의 User 모델을 확장하기 위해 AbstractUser 클래스를 상속해 값을 추가
    username = None
    email = models.EmailField(_('email address'), unique=True) # 이메일 필드를 추가하고 username 필드를 삭제
    # profile_img = models.ImageField(upload_to='profile_img', blank=True)  # 프로필 이미지
    # feed = models.ForeignKey(Feed, on_delete=models.CASCADE, blank=True) # 내가 쓴 피드
    # scrap = models.ForeignKey(Article, on_delete=models.CASCADE, blank=True) # 스크랩한 기사
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True) # 선호하는 카테고리

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email



# 마이페이지, 프로필 설정용 모델
# 내가 쓴 피드, 스크랩한 기사, 닉네임 변경, 프로필 이미지 등록, 변경, 비밀번호 변경, 선호하는 카테고리 수정 등


# 커뮤니티에 들어갈 것.  < - Feed 모델을 여기서 참조해야 하기 때문.
# class Feed(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)