from django.urls import path, include
from rest_framework import urls
from .views import *
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'accounts'


router = routers.DefaultRouter()
router.register('list', UserViewSet)    # 유저리스트 (테스트용)

urlpatterns = [
    path("register/", RegisterAPIView.as_view()),
    path("auth/", AuthAPIView.as_view()),               # post-로그인, delete-로그아웃, get-유저정보
    path("auth/refresh/", TokenRefreshView.as_view()),  # jwt 토큰 재발급
    path("", include(router.urls)),

    # 구글 소셜로그인
    path("google/login", google_login, name='google_login'),
    path('google/callback/', google_callback, name='google_callback'),
    path('google/login/finish/', GoogleLogin.as_view(), name='google_login_todjango'),
]