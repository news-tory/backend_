from django.core import serializers
from rest_framework import serializers
from .models import Post, Comment, Post_Like

class PostSerializer(serializers.ModelSerializer):
    # user = serializers.CharField(source='user.nickname', read_only=True)
    # class Meta:
    #     model = Post
    #     fields = ['id', 'user', 'content', 'created_at', 'like_cnt', 'article']
    # 위처럼 짜면 like_cnt가 0으로 나옴
    # 아래처럼 짜야 like_cnt가 실시간으로 바뀜
    user = serializers.CharField(source='user.nickname', read_only=True)
    like_cnt = serializers.IntegerField(source='post_like_set.count', read_only=True)
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
    like_cnt = serializers.IntegerField(source='post_like_set.count', read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'created_at', 'like_cnt', 'comments', 'article']

class PostLikeSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.nickname', read_only=True)
    class Meta:
        model = Post_Like
        fields = '__all__'
    
    def create(self, validated_data):
        post_like, created = Post_Like.objects.get_or_create(
            post=validated_data['post'],
            user=validated_data['user']
        )
        if not created:
            post_like.delete()
        return post_like