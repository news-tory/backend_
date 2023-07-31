from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
base_url = 'https://content.guardianapis.com/search'

# @csrf_exempt
class InitDBView(APIView):
    def get(self, request):
        url = f'{base_url}?api-key=113f18c4-cb4f-4a81-a86b-8e79acaba7a6'
        res = requests.get(url)
        articles = res.json()['response']['results']


        for article in articles:
            news_data = Article()
            news_data.title = article['webTitle']
            news_data.url = article['webUrl']
            # news_data.date = article['webPublicationDate']
            news_data.section = article['sectionName']
            news_data.save()
        
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

