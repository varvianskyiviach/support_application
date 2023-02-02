from django.http import JsonResponse
from rest_framework import status
from rest_framework.viewsets import ViewSet

from shared.django import ResponceMultiSerializer, ResponceSerializer
from tickets.models import Ticket
from tickets.serializers import TicketLightSerializer, TicketSerializer


class TicketAPISet(ViewSet):
    def list(self, request):
        queryset = Ticket.objects.all()
        serializer = TicketSerializer(queryset, many=True)
        responce = ResponceMultiSerializer({"results": serializer.data})
        return JsonResponse(responce.data)

    def retrieve(self, request, pk):
        instance = Ticket.objects.get(id=pk)
        serializer = TicketLightSerializer(instance)
        responce = ResponceSerializer({"result": serializer.data})
        return JsonResponse(responce.data)

    def create(self, request):
        context: dict = {
            "request": self.request,
        }
        serializer = TicketSerializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        responce = ResponceSerializer({"result": serializer.data})
        return JsonResponse(responce.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        context: dict = {
            "request": self.request,
        }
        queryset = Ticket.objects.get(id=pk)
        serializer = TicketSerializer(queryset, data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        responce = ResponceSerializer({"result": serializer.data})
        return JsonResponse(responce.data)
