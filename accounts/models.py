from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# class OverwriteStorage(FileSystemStorage):
#     '''
#     file 같은 이름 존재할 경우 overwrite
#     '''
#     def get_available_name(self, name, max_length=None):
#         if self.exists(name):
#             os.remove(os.path.join(settings.MEDIA_ROOT, name))
#         return name

# 헬퍼 클래스
class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        주어진 이메일, 비밀번호 등 개인정보로 인스턴스 생성
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        """
        주어진 이메일, 비밀번호 등 개인정보로 User 인스턴스 생성
        단, 최상위 사용자이므로 권한을 부여
        """
        superuser = self.create_user(
            email=email,
            password=password,
        )

        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True

        superuser.save(using=self._db)
        return superuser


# AbstractBaseUser를 상속해서 유저 커스텀
class User(AbstractBaseUser, PermissionsMixin):
    
    nickname = models.CharField(max_length=120, unique=True, null=False, blank=False)
    email = models.EmailField(max_length=30, unique=True, null=False, blank=False)
    userImg = models.ImageField(upload_to="user", null=True, default="default_image.png")   #storage=OverwriteStorage(), 
    Sport = models.BooleanField(default=False)
    World = models.BooleanField(default=False)
    Art = models.BooleanField(default=False)
    Film = models.BooleanField(default=False)
    Society = models.BooleanField(default=False)
    Books = models.BooleanField(default=False)
    Business = models.BooleanField(default=False)
    Tech = models.BooleanField(default=False)
    Culture = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 헬퍼 클래스 통해 유저 생성
        # 일반 유저를 만들 때는 create_user(), 관리자 계정을 만들 때는 create_superuser()를 탐
    objects = UserManager()

    # 사용자의 username field는 email으로 설정 (이메일로 로그인)
    USERNAME_FIELD = 'email'