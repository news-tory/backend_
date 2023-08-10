from django.urls import path
from .views import *

app_name = 'articles'

# urlpatterns = [
#     path('guardian/', GUARDIAN_View.as_view()),
#     path('guardian/init/', init_Guardian_db),
#     path('nyt/', NYTView.as_view()),
#     path('nyt/init/', init_NYT_db),
#     path('guardian/<int:pk>/', GuardianDetail.as_view()),
#     path('nyt/<int:pk>/', NYTDetail.as_view()),
#     path('guardian/<int:pk>/comments/', GuardianComment.as_view(), name='guardian-comments'),
#     path('nyt/<int:pk>/comments/', NYTComment.as_view(), name='nyt-comments'),
# ]


urlpatterns = [
    path('', ArticleView.as_view()),
    path('init/', init_integrate_db),
]