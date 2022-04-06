import imp
from urllib import response
from django.shortcuts import render
from functions.api import apiCall
from functions.summary import summarize
from functions.sentiment import sentiment, subjectivity
from functions.get_photo import get_photo
api_data = {}


# def add_summary():
#     global api_data
#     # print(api_data)
#     summary = []
#     for i in range(10):
#         try:
#             description = api_data["results"][i]["description"]
#             content=api_data["results"][i]["content"]
#             full_description=api_data["results"][i]["full_description"]
#             summary.append(summarize(description))
#         except:
#             summary.append(
#                 "Invalid API Response, no content or description provided by API.")
#         if sum
#     api_data["summary"] = []
#     api_data.update({"summary": summary})
def add_summary():
    global api_data
    summary = []
    for i in range(8):
        description = ""
        full_description = ""
        content = ""
        try:
            description = api_data["results"][i]["description"]
            length_des = len(description)
        except:
            description = ""
            length_des = 0
            print("excpet des "+str(i))
        try:
            full_description = api_data["results"][i]["full_description"]
            print(full_description)
            length_ful = len(full_description)
            print(length_ful)
        except:
            full_description = ""
            length_ful = 0
            print("excpet full "+str(i))
        try:
            content = api_data["results"][i]["content"]
            length_content = len(content)
        except:
            content = ""
            length_content = 0
            print("excpet content "+str(i))
        if length_content >= length_des and length_content >= length_ful and length_content != 0:
            summary.append(summarize(content))
        elif length_des >= length_content and length_des >= length_ful and length_des != 0:
            summary.append(description)
        elif length_ful >= length_content and length_ful >= length_des and length_ful != 0:
            print(str(full_description)+" "+str(i))
            summary.append(summarize(full_description))
        else:
            summary.append(
                "Content of proper is not provided by API to summarize properly")
    api_data["summary"] = []
    api_data.update({"summary": summary})


def add_sentiment():
    global api_data
    sentiment_data = []
    for i in range(8):
        description = ""
        full_description = ""
        content = ""
        try:
            description = api_data["results"][i]["description"]
            length_des = len(description)
        except:
            description = ""
            length_des = 0
        try:
            full_description = api_data["results"][i]["full_description"]
            length_ful = len(full_description)
        except:
            full_description = ""
            length_ful = 0
        try:
            content = api_data["results"][i]["content"]
            length_content = len(content)
        except:
            content = ""
            length_content = 0
        if length_content > length_des and length_content > length_ful:
            sentiment_data.append(sentiment(content))
        elif length_des > length_content and length_des > length_ful:
            sentiment_data.append(sentiment(description))
        elif length_ful > length_content and length_ful > length_des:
            sentiment_data.append(sentiment(full_description))
        else:
            sentiment_data.append("Neutral")

    api_data["sentiment"] = []
    api_data.update({"sentiment": sentiment_data})


def add_subjectivity():
    global api_data
    subjectivity_data = []
    for i in range(10):
        description = ""
        full_description = ""
        content = ""
        try:
            description = api_data["results"][i]["description"]
            length_des = len(description)
        except:
            description = ""
            length_des = 0
        try:
            full_description = api_data["results"][i]["full_description"]
            length_ful = len(full_description)
        except:
            full_description = ""
            length_ful = 0
        try:
            content = api_data["results"][i]["content"]
            length_content = len(content)
        except:
            content = ""
            length_content = 0
        if length_content > length_des and length_content > length_ful:
            subjectivity_data.append(subjectivity(content))
        elif length_des > length_content and length_des > length_ful:
            subjectivity_data.append(subjectivity(description))
        elif length_ful > length_content and length_ful > length_des:
            subjectivity_data.append(subjectivity(full_description))
        else:
            subjectivity_data.append(0)
    api_data["subjectivity"] = []
    api_data.update({"subjectivity": subjectivity_data})

# Create your views here.


def index(request):
    data = apiCall()
    global api_data
    api_data = data
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
