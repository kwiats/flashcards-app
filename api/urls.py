from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token


from . import views


urlpatterns = [
    path(
        "auth-token/",
        obtain_auth_token,
        name="obtain-auth-token",
    ),
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
        "user/",
        views.UserListView.as_view(),
        name="all-users",
    ),
    path(
        "user/<int:pk>/",
        views.UserDetailView.as_view(),
        name="specific-user",
    ),
    path(
        "user/<int:pk>/change-password/",
        views.ChangePasswordView.as_view(),
        name="change-password",
    ),
    path(
        "ranking/",
        views.RankingListView.as_view(),
        name="score-ranking",
    ),
    path(
        "user/<int:pk>/score/total_score",
        views.ScoreUserView.as_view(),
        name="total_user_score",
    ),
    path(
        "user/<int:pk>/score/spend_score",
        views.ScoreUserView.as_view(),
        name="spend_user_score",
    ),
    path(
        "user/<int:pk>/score/current_score",
        views.ScoreUserView.as_view(),
        name="current_user_score",
    ),
]
