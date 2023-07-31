from django.urls import path
from .views import *

app_name = 'articles'

urlpatterns = [
    path('', InitDBView.as_view()),
    path('nyt/', NYTView.as_view()),
    path('nyt/init/', init_NYT_db),
    # path('list/', ArticleListView.as_view(), name='article-list'),
]