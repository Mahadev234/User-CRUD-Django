from django.urls import path
from . import views

urlpatterns = [
    path("users", views.create_user, name="get or create users"),
]
