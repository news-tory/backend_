from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser): # 장고의 User 모델을 확장하기 위해 AbstractUser 클래스를 상속해 값을 추가
    REQUIRED_FIELDS = []
    email = None
    nickname = models.CharField(max_length=100)
    university = models.CharField(max_length=50)
    location = models.CharField(max_length=200)