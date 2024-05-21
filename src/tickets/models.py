from django.conf import settings
from django.db import models

from shared.django import TimeStampMixin


class Ticket(TimeStampMixin):
    customer = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name="customer_tickets",
    )
    manager = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        null=True,
        default=None,
        on_delete=models.DO_NOTHING,
        related_name="manager_tickets",
    )

    heder = models.CharField(max_length=255)
    body = models.TextField()
