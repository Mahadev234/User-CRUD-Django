from django.shortcuts import render
from django.http import HttpResponse, QueryDict
from django.template import loader
from rest_framework.decorators import api_view

from .forms import AddForm, UpdateForm

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
            response = requests.post(
                "http://127.0.0.1:8000/api/users", data=serializer.validated_data
            )
            if response.status_code == 201:
                context = {"message": "User added successfully"}
                return render(request, "status.html", context)
            else:
                context = {"message": "User not added"}
                return render(request, "status.html", context)
        else:
            context = {"message": "User not added"}
            return render(request, "status.html", context)


@api_view(["GET", "POST"])
def update(request, id):
    data = requests.get(f"http://127.0.0.1:8000/api/users/{id}").json()
    if request.method == "GET":
        template = loader.get_template("updateDelete.html")
        context = {"form": UpdateForm(data=data), "data": data}
        return HttpResponse(template.render(context, request))
    elif request.method == "POST":
        data = requests.put(
            f"http://127.0.0.1:8000/api/users/{id}", data=request.data
        ).json()
        context = {"message": "User updated successfully"}
        return render(request, "status.html", context)
