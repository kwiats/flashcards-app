from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add_word/", views.add_word, name="add_word"),
    path("add_category/", views.add_category, name="add_category"),
    path("test/", views.flashcards, name="flashcards"),
]
