from rest_framework import serializers

from comments.models import Comment
from tickets.models import Ticket


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["user", "ticket", "prev_comment"]

    def create(self, validated_data):

        request = self.context["request"]
        ticket_id: int = request.parser_context["kwargs"]["ticket_id"]
        ticket: Ticket = Ticket.objects.get(id=ticket_id)

        last_comment: Comment | None = ticket.comments.last()

        validated_data["ticket"] = ticket
        validated_data["user"] = request.user
        validated_data["prev_comment"] = last_comment

        comment = Comment(**validated_data)
        comment.save()

        return comment
