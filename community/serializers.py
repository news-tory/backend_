from django.core import serializers
from rest_framework import serializers
from .models import Post, Comment, Post_Like

class PostSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.nickname', read_only=True)
    like_cnt = serializers.IntegerField(source='post_like_set.count', read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'created_at', 'like_cnt', 'article', 'is_liked']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.nickname', read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'post_id', 'user', 'created_at', 'content']


class PostDetailSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.nickname', read_only=True)
    comments = CommentSerializer(many=True, read_only=True, source='comment_set')
    like_cnt = serializers.IntegerField(source='post_like_set.count', read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'created_at', 'like_cnt', 'comments', 'article', 'is_liked']


class PostLikeSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.nickname', read_only=True)
    class Meta:
        model = Post_Like
        fields = '__all__'
    
    # post_like_set을 사용하기 위해, create 메소드를 오버라이딩
    # post_like_set은 related_name으로 설정해준 것
    def create(self, validated_data):
        post_like, created = Post_Like.objects.get_or_create(
            post=validated_data['post'],
            user=validated_data['user']
        )
        # 이미 좋아요를 누른 상태에서 다시 누르면 좋아요 취소
        if not created:
            post_like.delete()
        return post_like