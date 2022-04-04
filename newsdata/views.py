import imp
from turtle import title
from urllib import response
from django.shortcuts import render, HttpResponse
from functions.api import apiCall
from functions.summary import summarize
from functions.sentiment import sentiment
# Create your views here.


def index(request):
    data = apiCall()
    # print(data])
    return render(request, "index.html", data)
