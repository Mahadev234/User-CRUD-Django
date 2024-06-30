from django.urls import path
from . import views

urlpatterns = [
    path("users", views.create_user, name="get or create users"),
    path(
        "users/<int:id>",
        views.rud_user_details,
        name="get, update or delete a single user details",
    ),
]
