from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("{{cookiecutter.project_slug}}.urls")),
    path("", include("globus_portal_framework.urls")),
    path("", include("social_django.urls", namespace="social")),
]
