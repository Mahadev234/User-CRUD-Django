from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import requests


def index(request):
    template = loader.get_template("index.html")
    data = requests.get("http://127.0.0.1:8000/api/users").json()
    context = {
        "users": data,
    }
    return HttpResponse(template.render(context, request))
