from django.urls import path
from .views import *

app_name = 'articles'

urlpatterns = [
    path('', InitDBView.as_view()),
    # path('list/', ArticleListView.as_view(), name='article-list'),
]