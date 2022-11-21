from django.urls import path, include
from . import views

from .api_views import WordListView, WordDetailView
from rest_framework import routers
from .rest_views import WordViewSet, CategoryViewSet, AnswerViewSet, UserViewSet


urlpatterns = [
    # api
    path("word/", WordListView.as_view()),
    path("word/<int:pk>/", WordDetailView.as_view()),
    # front
    # path("", views.home, name="home"),
    # path("add_word/", views.add_word, name="add_word"),
    # path("add_category/", views.add_category, name="add_category"),
    # path("home/", views.flashcards, name="flashcards"),
]
