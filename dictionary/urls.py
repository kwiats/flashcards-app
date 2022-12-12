"""dictionary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


schema_view = get_schema_view(
    openapi.Info(
        title="flashcards.app API",
        default_version="v0.0.1",
        description="Flashcards application is built for learning English vocabulary for Poles. By application, users can choose between 4 options(3 random translated word and 1 correct translated word), then application check your option with main transaltion. Application can give you some points for fastibility and good choice. It is possible to set vocabulary repetitions for the user. Users can show up your statistics about knows vocabulary.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="kontakt.pawelkwiatkowski@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    urlconf="api.urls",
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("cards.urls")),
    path("api/", include("api.urls")),
    path("api/schema.yaml/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
