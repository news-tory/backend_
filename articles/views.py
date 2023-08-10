import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer
from django.conf import settings





class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all().order_by('id')
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




# class GuardianDetail(APIView):
#     def get(self, request, pk):
#         article = get_object_or_404(Guardian, pk=pk)
#         serializer = GuardianSerializer(article)
#         return Response(serializer.data)
