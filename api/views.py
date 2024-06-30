# from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


@api_view(["GET", "POST"])
def create_user(request):
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET", "PUT", "DELETE"])
def rud_user_details(request):
    if request.method == "PUT":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            instance = User.objects.get(id=request.data["id"])
            serializer.update(instance, request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "GET":
        user = User.objects.get(id=request.data["id"])
        if user:
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("User not found", status=status.HTTP_404_NOT_FOUND)

    elif request.method == "DELETE":
        user = User.objects.get(id=request.data["id"])
        if user:
            user.delete()
            return Response("User deleted", status=status.HTTP_200_OK)
        else:
            return Response("User not found", status=status.HTTP_404_NOT_FOUND)
