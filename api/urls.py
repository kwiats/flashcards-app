from django.urls import path

from .views import (
    WordListView,
    WordDetailView,
    CategoryListView,
    CategoryDetailView,
    UserListView,
    UserDetailView,
    RankingListView,
    ChangeEmailView,
    ChangePasswordView,
)


urlpatterns = [
    path("word/", WordListView.as_view(), name="all-words"),
    path("word/<int:pk>/", WordDetailView.as_view(), name="single-word"),
    path("category/", CategoryListView.as_view(), name="all-categories"),
    path("category/<int:pk>/", CategoryDetailView.as_view(), name="single-category"),
    path("user/", UserListView.as_view(), name="all-users"),
    path("user/<int:pk>/", UserDetailView.as_view(), name="specific-user"),
    # path(
    #     "user/<int:pk>/change-email/",
    #     ChangeEmailView.as_view(),
    #     name="change-email",
    # ),
    path(
        "user/<int:pk>/change-password/",
        ChangePasswordView.as_view(),
        name="change-password",
    ),
    path("ranking/", RankingListView.as_view(), name="score-ranking"),
    # path("/user/<int:pk>/score"),
    # path("/user/<int:pk>/score/add-points"),
]
