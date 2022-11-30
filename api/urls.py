from django.urls import path

from .views import (
    WordListView,
    WordDetailView,
    CategoryListView,
    CategoryDetailView,
    UserListView,
)


urlpatterns = [
    path("word/", WordListView.as_view()),
    path("word/<int:pk>/", WordDetailView.as_view()),
    path("category/", CategoryListView.as_view()),
    path("category/<int:pk>/", CategoryDetailView.as_view()),
    path("user/", UserListView.as_view()),
]
