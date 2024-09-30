from django.shortcuts import render, get_object_or_404
from news.models import News


# Create your views here.
def index(request):
    news_list = News.objects.all()
    return render(request, "home.html", {'news_list': news_list})


def news_details(request, id):
    news_item = get_object_or_404(News, id=id)
    return render(request, 'news_details.html', {'news': news_item})
