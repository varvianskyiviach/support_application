from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet

from shared.django import ResponceMultiSerializer, ResponceSerializer
from users.models import User
from users.serializers import UserSerializer, UserUpdateSerializer


class UserAPISet(ViewSet):
    permission_classes = [AllowAny]

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        responce = ResponceMultiSerializer({"results": serializer.data})
        return JsonResponse(responce.data)

    def retrieve(self, request, pk):
        instance = User.objects.get(id=pk)
        serializer = UserSerializer(instance)
        responce = ResponceSerializer({"result": serializer.data})
        return JsonResponse(responce.data)

    def create(self, request):
        context: dict = {
            "request": self.request,
        }
        serializer = UserSerializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        responce = ResponceSerializer({"result": serializer.data})
        return JsonResponse(responce.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        context: dict = {
            "request": self.request,
        }
        instance = User.objects.get(id=pk)
        serializer = UserUpdateSerializer(instance, data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        responce = ResponceSerializer({"result": serializer.data})
        return JsonResponse(responce.data)
