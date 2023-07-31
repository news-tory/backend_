from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


base_url = 'https://content.guardianapis.com/search'

# @csrf_exempt
class InitDBView(APIView):
    def get(self, request):
        url = f'{base_url}?api-key={settings.GUARDIAN_API_KEY}'
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


def init_NYT_db(request):
    url = "https://api.nytimes.com/svc/topstories/v2/home.json?api-key={settings.NYT_API_KEY}"
    res = requests.get(url)
    articles = res.json()['results']
    for article in articles:
        news_data = Article()
        news_data.title = article['title']
        news_data.abstract = article['abstract']
        news_data.url = article['url']
        news_data.img_url = article['multimedia'][0]['url']
        news_data.section = article['section']
        news_data.paper = 'NYT'
        news_data.save()
        
class NYTView(APIView):
    def get(self, request):
        articles = Article.objects.filter(paper='NYT')
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)