from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index page"),
    path("add/", views.add_user, name="add_user page"),
]
