from django.http import JsonResponse
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from shared.django import ResponceMultiSerializer, ResponceSerializer
from tickets.models import Ticket
from tickets.permissions import IsOwner, RoleIsAdmin, RoleIsManager, RoleIsUser
from tickets.serializers import TicketLightSerializer, TicketSerializer


class TicketAPISet(ModelViewSet):
    queryset = Ticket.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return TicketLightSerializer

        return TicketSerializer

    def get_permissions(self):

        if self.action == "list":
            permission_classes = [RoleIsAdmin | RoleIsManager]
        elif self.action == "create":
            permission_classes = [RoleIsUser]
        elif self.action == "retrieve":
            permission_classes = [IsOwner | RoleIsManager | RoleIsAdmin]
        else:
            permission_classes = [RoleIsManager | RoleIsAdmin]

        return [permission() for permission in permission_classes]

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        responce = ResponceMultiSerializer({"results": serializer.data})

        return JsonResponse(responce.data)

    def retrieve(self, request, pk):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        responce = ResponceSerializer({"result": serializer.data})

        return JsonResponse(responce.data)

    def create(self, request):
        context: dict = {"request": self.request}
        serializer = self.get_serializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        responce = ResponceSerializer({"result": serializer.data})

        return JsonResponse(responce.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        instance = self.get_object()

        context: dict = {"request": self.request}
        serializer = self.get_serializer(instance, data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        responce = ResponceSerializer({"result": serializer.data})

        return JsonResponse(responce.data)

    def destroy(self, request, pk):
        instance = self.get_object()
        self.perform_destroy(instance=instance)

        return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
