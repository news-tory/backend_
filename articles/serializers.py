from rest_framework import serializers
from .models import Article, Article_Like
from community.models import Post


class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.nickname', read_only=True)
    like_cnt = serializers.IntegerField(source='article_like.count', read_only=True)
    post_cnt = serializers.IntegerField(source='article_post_set.count', read_only=True)
    popularity = serializers.SerializerMethodField()
    user_like = serializers.SerializerMethodField()


    class Meta:
        model = Article
        fields = ['id', 'user', 'title', 'abstract', 'url', 'img_url', 'section', 'paper', 
                  'published_date', 'like_cnt', 'post_cnt', 'popularity', 'user_like' ]
    
    def get_popularity(self, obj):
        return obj.article_post_set.count() + obj.article_like.count()
    
    def get_user_like(self, obj):
        request = self.context.get('request', None)
        if request and request.user.is_authenticated:
            return obj.article_like.filter(user=request.user).exists()
        return False


class ArticleLikeSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.nickname', read_only=True)
    class Meta:
        model = Article_Like
        fields = '__all__'
    
    def create(self, validated_data):
        post_like, created = Article_Like.objects.get_or_create(
            post=validated_data['post'],
            user=validated_data['user']
        )
        if not created:
            post_like.delete()
        return post_like