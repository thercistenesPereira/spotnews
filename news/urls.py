from django.urls import path, include
from news.views import (
    index,
    news_details,
    category_form,
    news_form_view,
    CategoryViewSet,
    UserViewSet,
)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path("", index, name="home-page"),
    path("news/<int:id>/", news_details, name="news-details-page"),
    path("categories/", category_form, name="categories-form"),
    path("news/", news_form_view, name="news-form"),
    path("api/", include(router.urls)),
]
