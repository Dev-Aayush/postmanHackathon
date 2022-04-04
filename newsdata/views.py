from asyncio.windows_events import NULL
import imp
from turtle import clear, title
from urllib import response
from django.shortcuts import render, HttpResponse
from functions.api import apiCall
from functions.summary import summarize
from functions.sentiment import sentiment
# Create your views here.
api_data = {}


def add_summary():
    global api_data
    summary = []
    for i in range(0, 9):
        description = api_data["results"][i]["content"]
        if description == None:
            description = api_data["results"][i]["full_description"]
        # print(str(i)+description)
        summary.append(summarize(description))
    # print(summary)
    api_data["summary"] = []
    api_data.update({"summary": summary})


def add_sentiment():
    global api_data
    sentiment_data = []
    for i in range(0, 9):
        description = api_data["results"][i]["content"]
        if description == None:
            description = api_data["results"][i]["full_description"]
        sentiment_data.append(sentiment(description))
    api_data["sentiment"] = []
    api_data.update({"sentiment": sentiment_data})


def index(request):
    data = apiCall()
    global api_data
    api_data = data
    add_summary()
    add_sentiment()
    return render(request, "index.html", api_data)


def about(request):
    print(api_data)
    return render(request, "about.html")


def first(request):
    global api_data
    return render(request, "first.html", api_data)


def second(request):
    global api_data
    return render(request, "second.html", api_data)


def third(request):
    global api_data
    return render(request, "third.html", api_data)


def fourth(request):
    global api_data
    return render(request, "fourth.html", api_data)


def fifth(request):
    global api_data
    return render(request, "fifth.html", api_data)


def sixth(request):
    global api_data
    return render(request, "sixth.html", api_data)


def seventh(request):
    global api_data
    return render(request, "seventh.html", api_data)


def eighth(request):
    global api_data
    return render(request, "eigth.html", api_data)
