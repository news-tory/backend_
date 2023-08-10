from django.core import serializers
from rest_framework import serializers
from .models import Post, Comment, Post_Like

class PostSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.nickname', read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'created_at', 'like_cnt', 'article']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.nickname', read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'post_id', 'user', 'created_at', 'content', 'like_cnt']
        
class PostDetailSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.nickname', read_only=True)
    comments = CommentSerializer(many=True, read_only=True, source='comment_set')
    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'created_at', 'like_cnt', 'comments', 'article']

class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post_Like
        fields = '__all__'