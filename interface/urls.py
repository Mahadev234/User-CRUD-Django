from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index page"),
    path("add/", views.add_user, name="add_user page"),
    path("update/<int:id>", views.update_user, name="update page"),
    path("delete/<int:id>", views.delete_user, name="delete page"),
]
