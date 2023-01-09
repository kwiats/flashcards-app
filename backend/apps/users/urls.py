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
        "user/<int:pk>/score/",
        views.ScoreUserView.as_view(),
        name="total-user-score",
    ),
]
