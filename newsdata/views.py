import imp
from urllib import response
from django.shortcuts import render
from functions.api import apiCall
from functions.summary import summarize
from functions.sentiment import sentiment, subjectivity
from functions.get_photo import get_photo
api_data = {}


def add_summary():
    global api_data
    # print(api_data)
    summary = []
    for i in range(10):
        try:
            description = api_data["results"][i]["content"]
            if description == None:
                description = api_data["results"][i]["description"]
            if description == None:
                description = api_data["results"][i]["full_description"]
            print(str(i)+"  "+description)
            summary.append(summarize(description))
        except:
            summary.append(
                "Invalid API Response, no content or description provided by API.")
    api_data["summary"] = []
    api_data.update({"summary": summary})


def add_sentiment():
    global api_data
    sentiment_data = []
    for i in range(10):
        try:
            description = api_data["results"][i]["content"]
            if description == None:
                description = api_data["results"][i]["description"]
            if description == None:
                description = api_data["results"][i]["full_description"]
            sentiment_data.append(sentiment(description))
        except:
            sentiment_data.append("InvdAPIres")
    api_data["sentiment"] = []
    api_data.update({"sentiment": sentiment_data})


def add_subjectivity():
    global api_data
    subjectivity_data = []
    for i in range(10):
        try:
            description = api_data["results"][i]["content"]
            if description == None:
                description = api_data["results"][i]["description"]
            if description == None:
                description = api_data["results"][i]["full_description"]
            subjectivity_data.append(int(subjectivity(description)))
        except:
            subjectivity_data.append("InvdAPIres")
    api_data["subjectivity"] = []
    api_data.update({"subjectivity": subjectivity_data})

# Create your views here.


def index(request):
    data = apiCall()
    global api_data
    api_data = data
    print(api_data)
    add_summary()
    add_sentiment()
    add_subjectivity()
    return render(request, "index.html", api_data)


def about(request):
    photo = get_photo()
    return render(request, "about.html", photo)


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
    return render(request, "eighth.html", api_data)
