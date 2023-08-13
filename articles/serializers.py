from rest_framework import serializers
from .models import Article



class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'abstract', 'url', 'img_url', 'section', 'paper', 'published_date']

