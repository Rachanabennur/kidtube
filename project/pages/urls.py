# pages/urls.py
from unicodedata import name
# from django import views
from pages import views
from django.urls import path
from .views import HomePageView, AboutPageView, LoginPageView, upload, index


urlpatterns = [
    path("", index, name="index"),
    path("home", HomePageView, name="home"),
    path("about/", AboutPageView, name="about"),
    path('upload', upload, name="upload"),
#     path('login/', LoginPageView.as_view(
#     authentication_form=CustomLoginForm),
#     name="login"
#   )

    path("", LoginPageView, name="login")
]