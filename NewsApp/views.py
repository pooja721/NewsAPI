from django.shortcuts import render
from newsapi.newsapi_client import NewsApiClient



# Create your views here.
def Index(request):
    newsapi = NewsApiClient(api_key="fa4ae8ffbcc04cc6bf11d166b9487b5a")
    topheadlines = newsapi.get_top_headlines(sources="the-times-of-india")

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        img.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, desc, img)


    return render(request, 'index.html', context={"mylist": mylist})

def bbc(request):
    newsapi = NewsApiClient(api_key="fa4ae8ffbcc04cc6bf11d166b9487b5a")
    topheadlines = newsapi.get_top_headlines(sources='the-times-of-india')

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, desc, img)

    return render(request, 'bbc.html', context={"mylist": mylist})