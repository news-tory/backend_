from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# 헬퍼 클래스
class UserManager(BaseUserManager):
    def create_user(self, nickname, email, password, **kwargs):
        """
        주어진 이메일, 비밀번호 등 개인정보로 인스턴스 생성
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            nickname=nickname,
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, nickname=None, email=None, password=None, **extra_fields):
        """
        주어진 이메일, 비밀번호 등 개인정보로 User 인스턴스 생성
        단, 최상위 사용자이므로 권한을 부여
        """
        superuser = self.create_user(
            nickname=nickname,
            email=email,
            password=password,
        )

<<<<<<< HEAD
class CustomUser(AbstractUser): # 장고의 User 모델을 확장하기 위해 AbstractUser 클래스를 상속해 값을 추가
    username = None
    email = models.EmailField(_('email address'), unique=True) # 이메일 필드를 추가하고 username 필드를 삭제
    # profile_img = models.ImageField(upload_to='profile_img', blank=True)  # 프로필 이미지
    # feed = models.ForeignKey(Feed, on_delete=models.CASCADE, blank=True) # 내가 쓴 피드
    # scrap = models.ForeignKey(Article, on_delete=models.CASCADE, blank=True) # 스크랩한 기사
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True) # 선호하는 카테고리
=======
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True
>>>>>>> 807a25ec25b30158713234bd35b391b560f3d99b

        superuser.save(using=self._db)
        return superuser

# AbstractBaseUser를 상속해서 유저 커스텀
"""
AbstractBaseUser 모델을 상속한 User 커스텀 모델은 
- 로그인 아이디로 이메일 주소를 사용하거나
- Django 로그인 절차가 아닌 다른 인증 절차를 직접 구현할 수 있음

<<<<<<< HEAD
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
=======
PermissionsMixin ...?
"""
class User(AbstractBaseUser, PermissionsMixin):
    
    nickname = models.CharField(max_length=120, unique=True, null=False, blank=False)
    email = models.EmailField(max_length=30, unique=True, null=False, blank=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 헬퍼 클래스 통해 유저 생성
        # 일반 유저를 만들 때는 create_user(), 관리자 계정을 만들 때는 create_superuser()를 탐
    objects = UserManager()

    # 사용자의 username field는 email으로 설정 (이메일로 로그인)
    # USERNAME_FIELD = 'email'
    USERNAME_FIELD = 'nickname'
>>>>>>> 807a25ec25b30158713234bd35b391b560f3d99b
