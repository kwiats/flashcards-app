from django.urls import path, include
from . import views

from .views import WordListView, WordDetailView
from rest_framework import routers


urlpatterns = [

    path("word/", WordListView.as_view()),
    path("word/<int:pk>/", WordDetailView.as_view()),
]
