# Generated by Django 4.1.5 on 2023-01-16 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tickets", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="ticket",
            old_name="heder",
            new_name="header",
        ),
    ]