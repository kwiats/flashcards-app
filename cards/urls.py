from django.urls import path, include
from . import views

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("test", views.test, name="test"),
    path("", views.home, name="home"),
    path("auth-token/", obtain_auth_token, name="obtain-auth-token"),
]
