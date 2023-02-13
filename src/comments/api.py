from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from comments.serializers import CommentSerializer
from tickets.models import Ticket
from users.constants import Role


class CreateListViewSet(ListModelMixin, CreateModelMixin, GenericViewSet):
    pass


class CommentAPISet(CreateListViewSet):
    serializer_class = CommentSerializer
    lookup_field = "ticket_id"
    lookup_url_kwarg = "ticket_id"

    def _get_tickets(self):

        role: Role = self.request.user.role

        if role == Role.ADMIN:
            return Ticket.objects.all()
        elif role == Role.MANAGER:
            return Ticket.objects.filter(manager=self.request.user)

        return Ticket.objects.filter(customer=self.request.user)

    def get_queryset(self):

        ticket_id: int = self.kwargs[self.lookup_field]
        tickets = self._get_tickets()
        ticket = get_object_or_404(tickets, id=ticket_id)

        comments = ticket.comments.all()

        return comments

    def create(self, request, *args, **kwargs):

        ticket = Ticket.objects.get(id=self.kwargs[self.lookup_field])
        if ticket.customer != request.user:
            return Response(
                {"error": "You must be customer of this ticket"},
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
