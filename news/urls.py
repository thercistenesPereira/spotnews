from django.urls import path
from news.views import index, news_details, category_form


urlpatterns = [
    path("", index, name="home-page"),
    path('news/<int:id>/', news_details, name='news-details-page'),
    path('categories/', category_form, name='categories-form'),
]
