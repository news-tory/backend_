import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer, ArticleLikeSerializer
from django.conf import settings
from community.models import Post
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication






class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all().order_by('-id')
        serializer = ArticleSerializer(articles, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class PopularityView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        sorted_articles = sorted(articles, key=lambda article: article.article_post_set.count() + article.article_like.count(), reverse=True)
        serializer = ArticleSerializer(sorted_articles, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ArticleDetail(APIView):
    def get(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class LikeArticle(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        serializer = ArticleLikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, post=post)
            Article.user_like = True
            Article.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


class UserLikeArticle(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request, nickname):
        liked_articles = Article.objects.filter(article_like__user__nickname=nickname)
        serializer = ArticleSerializer(liked_articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


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

    section_mapping = {
        'sports': 'Sport',
        'football': 'Sport',
        'sport': 'Sport',
        'nyregion': 'World',
        'australia-news': 'World',
        'uk-news': 'World',
        'us-news': 'World',
        'us': 'World',
        'world': 'World',
        'arts': 'Art',
        'fashion': 'Art',
        'movies': 'Film',
        'theater': 'Film',
        'film': 'Film',
        'home': 'Society',
        'insider': 'Society',
        'obituaries': 'Society',
        'opinion': 'Society',
        'politics': 'Society',
        'commentisfree': 'Society',
        'politics': 'Society',
        'society': 'Society',
        'environment': 'Society',
        'news': 'Society',
        'realestate': 'Society',
        'sundayreview': 'Society',
        'upshot': 'Society',
        'books/review': 'Books',
        'magazine': 'Books',
        't-magazine': 'Books',
        'business': 'Business',
        'money': 'Business',
        'automobiles': 'Tech',
        'science': 'Tech',
        'technology': 'Tech',
        'food': 'Culture',
        'health': 'Culture',
        'travel': 'Culture',
        'lifeandstyle': 'Culture',
        'music': 'Culture',
        'tv-and-radio': 'Culture',
    }
    
    for article in nyt_articles:
        try:
            news_data = Article()
            news_data.title = article['title']
            news_data.abstract = article['abstract']
            news_data.url = article['url']
            news_data.img_url = article['multimedia'][0]['url']
            section = article['section']
            news_data.section = section_mapping.get(section, 'etc')
            news_data.paper = 'NewYorkTimes'
            news_data.published_date = article['published_date']



            news_data.save()
        except:
            pass

        
        for article in guardian_articles:
            try:
                news_data = Article()
                news_data.title = article['webTitle']
                news_data.url = article['webUrl']
                section = article['sectionName']
                news_data.section = section_mapping.get(section, 'etc')
                news_data.paper = 'Guardian'

                news_data.save()
            except:
                pass



