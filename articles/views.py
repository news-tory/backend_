from django.shortcuts import render
import requests
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import NYT, Guardian, Guardian_Comment, NYT_Comment
from .serializers import NYTSerializer, GuardianSerializer, NYT_CommentSerializer, Guardian_CommentSerializer
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly






## 뉴욕타임즈 ##

def init_NYT_db(request):
    url = f"https://api.nytimes.com/svc/topstories/v2/home.json?api-key={settings.NYT_API_KEY}"
    res = requests.get(url)
    articles = res.json()['results']
    for article in articles:
        try:
            news_data = NYT()
            news_data.title = article['title']
            news_data.abstract = article['abstract']
            news_data.url = article['url']
            news_data.img_url = article['multimedia'][0]['url']
            news_data.section = article['section']
            news_data.paper = 'NYT'
            news_data.save()
        except:
            pass


class NYTView(APIView):
    def get(self, request):
        articles = NYT.objects.filter(paper='NYT')
        serializer = NYTSerializer(articles, many=True)
        return Response(serializer.data)
    

class NYTDetail(APIView):
    def get(self, request, pk):
        article = get_object_or_404(NYT, pk=pk)
        serializer = NYTSerializer(article)
        return Response(serializer.data)


class NYTComment(ListCreateAPIView):
    queryset = NYT_Comment.objects.all()
    serializer_class =NYT_CommentSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        article_id = self.kwargs['pk']
        return NYT_Comment.objects.filter(post=article_id)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user = user)



## 가디언 ##
def init_Guardian_db(request):
    url = f"https://content.guardianapis.com/search?api-key={settings.GUARDIAN_API_KEY}"
    res = requests.get(url)
    articles = res.json()['response']['results']
    for article in articles:
        try:
            news_data = Guardian()
            news_data.title = article['webTitle']
            news_data.url = article['webUrl']
            news_data.section = article['sectionName']
            news_data.save()
        except:
            pass



class GUARDIAN_View(APIView):
    def get(self, request):
        articles = Guardian.objects.all()
        serializer = GuardianSerializer(articles, many=True)
        return Response(serializer.data)


class GuardianComment(ListCreateAPIView):
    queryset = Guardian_Comment.objects.all()
    serializer_class = Guardian_CommentSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        article_id = self.kwargs['pk']
        return Guardian_Comment.objects.filter(post=article_id)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user = user)





class GuardianDetail(APIView):
    def get(self, request, pk):
        article = get_object_or_404(Guardian, pk=pk)
        serializer = GuardianSerializer(article)
        return Response(serializer.data)