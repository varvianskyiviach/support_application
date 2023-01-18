from django.http import JsonResponse
from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView

from tickets.models import Ticket
from tickets.serializers import (
    TicketCreateSerializer,
    TicketLightSerializer,
    TicketSerializer,
)


class TicketsGetList(ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketGetAPI(RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketLightSerializer
    lookup_field = "id"


@api_view(["POST"])
def create_ticket(request):
    serializer = TicketCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    # Ticket.objects.create(**serializer.validated_data)

    return JsonResponse(serializer.validated_data)


urlpatterns = [
    path("", TicketsGetList.as_view()),
    path("create", create_ticket),
    path("<int:id>", TicketGetAPI.as_view()),
]
