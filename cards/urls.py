from django.urls import path, include
from . import views

from .api_views import WordListView, WordDetailView
from rest_framework import routers


urlpatterns = [
    # api
    path("word/", WordListView.as_view()),
    path("word/<int:pk>/", WordDetailView.as_view()),
    # front
    path("", views.home, name="home"),
]
