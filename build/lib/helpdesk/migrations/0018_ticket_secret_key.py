# Generated by Django 2.2.16 on 2020-10-10 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("helpdesk", "0017_default_owner_on_delete_null"),
    ]

    operations = [
        migrations.AlterField(
            model_name="followup",
            name="public",
            field=models.BooleanField(
                blank=True,
                default=False,
                help_text="Public tickets are viewable by the submitter and all staff, but non-public tickets can only be seen by staff.",
                verbose_name="Public",
            ),
        ),
        migrations.AlterField(
            model_name="ignoreemail",
            name="keep_in_mailbox",
            field=models.BooleanField(
                blank=True,
                default=False,
                help_text="Do you want to save emails from this address in the mailbox? If this is unticked, emails from this address will be deleted.",
                verbose_name="Save Emails in Mailbox?",
            ),
        ),
        migrations.AlterField(
            model_name="queue",
            name="allow_email_submission",
            field=models.BooleanField(
                blank=True,
                default=False,
                help_text="Do you want to poll the e-mail box below for new tickets?",
                verbose_name="Allow E-Mail Submission?",
            ),
        ),
        migrations.AlterField(
            model_name="queue",
            name="allow_public_submission",
            field=models.BooleanField(
                blank=True,
                default=False,
                help_text="Should this queue be listed on the public submission form?",
                verbose_name="Allow Public Submission?",
            ),
        ),
        migrations.AlterField(
            model_name="queue",
            name="email_box_ssl",
            field=models.BooleanField(
                blank=True,
                default=False,
                help_text="Whether to use SSL for IMAP or POP3 - the default ports when using SSL are 993 for IMAP and 995 for POP3.",
                verbose_name="Use SSL for E-Mail?",
            ),
        ),
        migrations.AlterField(
            model_name="savedsearch",
            name="shared",
            field=models.BooleanField(
                blank=True,
                default=False,
                help_text="Should other users see this query?",
                verbose_name="Shared With Other Users?",
            ),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="on_hold",
            field=models.BooleanField(
                blank=True,
                default=False,
                help_text="If a ticket is on hold, it will not automatically be escalated.",
                verbose_name="On Hold",
            ),
        ),
        migrations.AlterField(
            model_name="ticketcc",
            name="can_update",
            field=models.BooleanField(
                blank=True,
                default=False,
                help_text="Can this CC login and update the ticket?",
                verbose_name="Can Update Ticket?",
            ),
        ),
        migrations.AlterField(
            model_name="ticketcc",
            name="can_view",
            field=models.BooleanField(
                blank=True,
                default=False,
                help_text="Can this CC login to view the ticket details?",
                verbose_name="Can View Ticket?",
            ),
        ),
    ]
