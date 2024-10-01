from django.shortcuts import render, get_object_or_404, redirect
from news.models import News
from .forms import CategoryForm
from .forms import NewsForm
from .models import Category, User
from .serializers import CategorySerializer, UserSerializer
from rest_framework import viewsets


# Create your views here.
def index(request):
    news_list = News.objects.all()
    return render(request, "home.html", {"news_list": news_list})


def news_details(request, id):
    news_item = get_object_or_404(News, id=id)
    return render(request, "news_details.html", {"news": news_item})


def category_form(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home-page")
    else:
        form = CategoryForm()

    return render(request, "categories_form.html", {"form": form})


def news_form_view(request):
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home-page")
    else:
        form = NewsForm()
    return render(request, "news_form.html", {"form": form})


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
