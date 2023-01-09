from django.urls import path

from . import views

urlpatterns = [
    path(
        "word/",
        views.WordListView.as_view(),
        name="all-words",
    ),
    path(
        "word/<int:pk>/",
        views.WordDetailView.as_view(),
        name="single-word",
    ),
    path(
        "word/<int:pk>/translations",
        views.WordTranslationsView.as_view(),
        name="word-translations",
    ),
    path(
        "category/",
        views.CategoryListView.as_view(),
        name="all-categories",
    ),
    path(
        "category/<int:pk>/",
        views.CategoryDetailView.as_view(),
        name="single-category",
    ),
    path(
        "translation/",
        views.TranslationListView.as_view(),
        name="all-translations",
    ),
    path(
        "translation/<int:pk>/",
        views.TranslationDetailView.as_view(),
        name="specific-translation",
    ),
]
