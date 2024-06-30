from django.shortcuts import render
from django.http import HttpResponse, QueryDict
from django.template import loader
from rest_framework.decorators import api_view
from api.serializers import UserSerializer
from .forms import AddForm

import requests


def index(request):
    template = loader.get_template("index.html")
    data = requests.get("http://127.0.0.1:8000/api/users").json()
    context = {
        "users": data,
    }
    return HttpResponse(template.render(context, request))


@api_view(["GET", "POST"])
def add_user(request):
    template = loader.get_template("addUser.html")
    if request.method == "GET":
        context = {
            "form": AddForm(),
        }
        return HttpResponse(template.render(context, request))
    elif request.method == "POST":
        if isinstance(request.data, QueryDict):
            data = request.data.dict()
        else:
            data = request.data
        phone = data.get("phone")
        if isinstance(phone, str) and phone.isdigit():
            data["phone"] = int(phone)
        elif isinstance(phone, list) and all(p.isdigit() for p in phone):
            data["phone"] = [int(p) for p in phone]

        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            response = requests.post(
                "http://127.0.0.1:8000/api/users", data=serializer.validated_data
            )
            return HttpResponse("User added successfully", response.json())
        else:
            print(serializer.errors)
            return HttpResponse("User not added")
