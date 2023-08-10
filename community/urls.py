from django.urls import path
from .views import *

app_name = 'community'

urlpatterns = [
    path('posts/', PostView.as_view()),
    path('posts/<int:post_id>/', PostDetailView.as_view()),
    path('posts/<int:post_id>/comment/', CommentView.as_view()),
    path('posts/<int:post_id>/comment/<int:comment_id>/', CommentDetailView.as_view()),
]