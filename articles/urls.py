from django.urls import path
from .views import *

app_name = 'articles'


urlpatterns = [
    path('', ArticleView.as_view()),
    path('<int:pk>/', ArticleDetail.as_view()),
    path('popularity/', PopularityView.as_view()),
    path('init/', init_integrate_db),
    path('<int:article_id>/likes/', LikeArticle.as_view()),
    path('like/user/<str:nickname>', UserLikeArticle.as_view()),
]