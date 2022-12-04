from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from . import views

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

schema_view = get_schema_view(
    openapi.Info(
        title="flashcards.app API",
        default_version="v0.0.1",
        description="Flashcards application is built for learning English vocabulary for Poles. By application, users can choose between 4 options(3 random translated word and 1 correct translated word), then application check your option with main transaltion. Application can give you some points for fastibility and good choice. It is possible to set vocabulary repetitions for the user. Users can show up your statistics about knows vocabulary.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="kontakt.pawelkwiatkowski@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("test", views.test, name="test"),
    path("", views.home, name="home"),
    path("auth-token/", obtain_auth_token, name="obtain-auth-token"),
    path(
        "swagger",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
