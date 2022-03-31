# Generated by Django 2.0.1 on 2018-09-07 21:22
from django.db import migrations, models
import helpdesk.models


def clear_secret_keys(apps, schema_editor):
    Ticket = apps.get_model("helpdesk", "Ticket")
    db_alias = schema_editor.connection.alias

    for ticket in Ticket.objects.using(db_alias).all():
        ticket.secret_key = ""
        ticket.save()


class Migration(migrations.Migration):

    dependencies = [
        ("helpdesk", "0018_ticket_secret_key"),
    ]

    operations = [
        migrations.AddField(
            model_name="ticket",
            name="secret_key",
            field=models.CharField(
                default=helpdesk.models.mk_secret,
                max_length=36,
                verbose_name="Secret key needed for viewing/editing ticket by non-logged in users",
            ),
        ),
        migrations.RunPython(clear_secret_keys),
    ]
