from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import AddForm, UpdateForm
import requests


def index(request):
    template = loader.get_template("index.html")
    try:
        response = requests.get("http://127.0.0.1:8000/api/users")
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()  # Try to parse JSON
    except requests.exceptions.HTTPError as http_err:
        data = {"error": f"HTTP error occurred: {http_err}"}
    except requests.exceptions.RequestException as req_err:
        data = {"error": f"Request exception occurred: {req_err}"}
    except ValueError as json_err:
        data = {"error": f"JSON decode error: {json_err}"}

    context = {"users": data} if isinstance(data, list) else {"users": []}
    return HttpResponse(template.render(context, request))


def add_user(request):
    template = loader.get_template("addUser.html")
    if request.method == "GET":
        context = {"form": AddForm()}
        return HttpResponse(template.render(context, request))
    elif request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            response = requests.post("http://127.0.0.1:8000/api/users", data=data)
            context = (
                {"message": "User added successfully"}
                if response.status_code == 201
                else {"message": "User not added"}
            )
            return render(request, "status.html", context)
        else:
            context = {"message": "Invalid form data"}
            return render(request, "status.html", context)


def update_user(request, id):
    if request.method == "GET":
        template = loader.get_template("updateDelete.html")
        data = requests.get(f"http://127.0.0.1:8000/api/users/{id}").json()
        form = UpdateForm(initial=data)
        context = {"form": form, "data": data}
        return HttpResponse(template.render(context, request))
    elif request.method == "POST":
        form = UpdateForm(request.POST)
        if form.is_valid():
            response = requests.put(
                f"http://127.0.0.1:8000/api/users/{id}", data=form.cleaned_data
            )
            context = (
                {"message": "User updated successfully"}
                if response.status_code == 200
                else {"message": "User not updated"}
            )
            return render(request, "status.html", context)
        else:
            context = {"message": "Invalid form data"}
            return render(request, "status.html", context)


def delete_user(request, id):
    response = requests.delete(f"http://127.0.0.1:8000/api/users/{id}")
    context = (
        {"message": "User deleted successfully"}
        if response.status_code == 200
        else {"message": "User not found"}
    )
    return render(request, "status.html", context)
