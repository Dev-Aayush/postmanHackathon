from django.contrib import admin
from django.urls import path, include
from newsdata import views

urlpatterns = [
    path("", views.index, name="home")
]
