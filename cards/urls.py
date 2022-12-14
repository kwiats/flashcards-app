from django.urls import path, include, re_path
from rest_framework import permissions

from . import views

from rest_framework import routers


urlpatterns = [
    path("", views.home, name="home"),
]
