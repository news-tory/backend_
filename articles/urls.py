from django.urls import path
from .views import *

app_name = 'articles'

urlpatterns = [
    path('guardian/', GUARDIAN_View.as_view()),
    path('guardian/init/', init_Guardian_db),
    path('nyt/', NYTView.as_view()),
    path('nyt/init/', init_NYT_db),
]