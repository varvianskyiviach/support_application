# Generated by Django 4.1.4 on 2023-01-09 21:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tickets", "0001_initial"),
        ("comments", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="ticket",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="tickets.ticket"),
        ),
    ]
