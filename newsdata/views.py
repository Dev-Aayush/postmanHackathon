import imp
from turtle import title
from urllib import response
from django.shortcuts import render, HttpResponse
import requests
from private import api_key
from functions.summary import summarize
# Create your views here.


def apiCall():

    base_url = "https://newsdata.io/api/1/news?apikey=" + \
        api_key+"&country=in&language=en"
    # print(base_url)
    response = requests.get(base_url)
    json_data = response.json() if response and response.status_code == 200 else None
    return json_data


def index(request):
    data = apiCall()
    # print(data])
    return render(request, "index.html", data)
