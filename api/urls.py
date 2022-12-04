from django.urls import path

from .views import (
    WordListView,
    WordDetailView,
    CategoryListView,
    CategoryDetailView,
    UserListView,
)


urlpatterns = [
    path("word/", WordListView.as_view(), name="all-words"),
    path("word/<int:pk>/", WordDetailView.as_view(), name="single-word"),
    path("category/", CategoryListView.as_view(), name="all-categories"),
    path("category/<int:pk>/", CategoryDetailView.as_view(), name="single-category"),
    path("user/", UserListView.as_view(), name="all-users"),
    path("user/<str:username>/", UserDetailView.as_view(), name="specific-user"),
    path("user/ranking/", RankingListView.as_view(), name="score-ranking"),
]
