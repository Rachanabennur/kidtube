# pages/urls.py
from unicodedata import name
# from django import views
from pages import views
from django.urls import path
from .views import HomePageView, index, videoplay, upload2


urlpatterns = [
    path("", index, name="index"),
    path("home", HomePageView, name="home"),
    # path('upload', upload, name="upload"),
    path('upload2', upload2, name="upload2"),
    path("videoplay/<int:id>", videoplay, name="videoplay")
]

