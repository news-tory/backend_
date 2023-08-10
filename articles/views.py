from django.shortcuts import render
import requests
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly




class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


def get_guardian_data(request):
    url = f"https://content.guardianapis.com/search?api-key={settings.GUARDIAN_API_KEY}"
    res = requests.get(url)
    articles = res.json()['response']['results']
    return articles


def get_nyt_data(request):
    url = f"https://api.nytimes.com/svc/topstories/v2/home.json?api-key={settings.NYT_API_KEY}"
    res = requests.get(url)
    articles = res.json()['results']
    return articles


def init_integrate_db(request):
        guardian_articles = get_guardian_data(request)
        nyt_articles = get_nyt_data(request)

        for article in nyt_articles:
            try:
                news_data = Article()
                news_data.title = article['title']
                news_data.abstract = article['abstract']
                news_data.url = article['url']
                news_data.img_url = article['multimedia'][0]['url']
                news_data.section = article['section']
                news_data.paper = 'NewYorkTimes'
                news_data.save()
            except:
                pass

        for article in guardian_articles:
            try:
                news_data = Article()
                news_data.title = article['webTitle']
                news_data.url = article['webUrl']
                news_data.section = article['sectionName']
                news_data.paper = 'Guardian'
                news_data.save()
            except:
                pass




# class GuardianDetail(APIView):
#     def get(self, request, pk):
#         article = get_object_or_404(Guardian, pk=pk)
#         serializer = GuardianSerializer(article)
#         return Response(serializer.data)
