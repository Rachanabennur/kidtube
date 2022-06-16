# pages/urls.py
from unicodedata import name
# from django import views
from pages import views
from django.urls import path
from .views import HomePageView, upload, index, videoplay


urlpatterns = [
    path("", index, name="index"),
    path("home", HomePageView, name="home"),
    path('upload', upload, name="upload"),
    path("videoplay/<int:id>", videoplay, name="videoplay")
]

