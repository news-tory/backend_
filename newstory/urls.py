"""
URL configuration for newstory project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from articles.views import *
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),

    path('articles/', include('articles.urls')),
    path('community/', include('community.urls')),

    path('accounts/', include('accounts.urls')),    # 커스텀 유저 모델
    path('accounts/', include('allauth.urls')), # 추가한 라이브러리 매핑
    path('accounts/', include('dj_rest_auth.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
] 