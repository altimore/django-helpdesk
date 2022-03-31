# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 19:27
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("helpdesk", "0014_usersettings_related_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="queue",
            name="permission_name",
            field=models.CharField(
                blank=True,
                editable=False,
                help_text="Name used in the django.contrib.auth permission system",
                max_length=72,
                null=True,
                verbose_name="Django auth permission name",
            ),
        ),
    ]
