from django.urls import path, include
from . import views

from rest_framework import routers
from .rest_views import WordViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r"words", WordViewSet)
router.register(r"categories", CategoryViewSet)

urlpatterns = [
    # api
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("", views.home, name="home"),
    path("add_word/", views.add_word, name="add_word"),
    path("add_category/", views.add_category, name="add_category"),
    path("home/", views.flashcards, name="flashcards"),
]
