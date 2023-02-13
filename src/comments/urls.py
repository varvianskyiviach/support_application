from django.urls import path

from comments.api import CommentAPISet

urlpatterns = [
    path(
        "tickets/<int:ticket_id>/comments/",
        CommentAPISet.as_view({"post": "create", "get": "list"}),
    ),
]
