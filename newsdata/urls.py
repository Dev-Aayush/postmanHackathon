from django.contrib import admin
from django.urls import path, include
from newsdata import views

urlpatterns = [
    path("about", views.about, name="about us"),
    path("", views.index, name="home"),
    path("first", views.first, name="first"),
    path("second", views.second, name="second"),
    path("third", views.third, name="third"),
    path("fourth", views.fourth, name="fourth"),
    path("fifth", views.fifth, name="fifth"),
    path("sixth", views.sixth, name="sixth"),
    path("seventh", views.seventh, name="seventh"),
    path("eighth", views.eighth, name="eighth"),
]
