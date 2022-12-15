from django.http import HttpResponse
from django.urls import path


def get_result(variebles):
    return HttpResponse("Hello")


urlpatterns = [
    path("result/", get_result),
]
