from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("add_word/", views.add_word, name="add_word"),
    path("add_category/", views.add_category, name="add_category"),
    path("", views.flashcards, name="flashcards"),
]
