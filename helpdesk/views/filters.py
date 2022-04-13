import django_filters
from django.db.models import Q
from django.utils.translation import gettext as _
from django_filters.filters import (BooleanFilter, DateFromToRangeFilter,
                                    OrderingFilter, RangeFilter)
from django_select2.forms import Select2MultipleWidget, Select2Widget

from ..models import Ticket


class TicketFilter(django_filters.FilterSet):

    status = django_filters.MultipleChoiceFilter(
        choices=list(Ticket.STATUS_CHOICES),
        help_text=_("Choose a status"),
        widget=Select2MultipleWidget,
    )

    date = DateFromToRangeFilter(
        label=_("Ticket date range"),
        help_text=_("Choose the first and/or last ticket date to include."),
        method="filter_by_date",
    )
    sort = OrderingFilter(
        # tuple-mapping retains order
        fields=(
            ("created", "created"),
            ("title", "title"),
            ("queue", "queue"),
            ("status", "status"),
            ("priority", "priority"),
            ("owner", "owner"),
        ),
        # labels do not need to retain order
        # field_labels={
        #     "username": "User account",
        # },
    )

    def filter_by_date(self, qs, name, value):
        start_date = value.start
        end_date = value.stop

        # qs = qs.annotate_date()
        if start_date:
            qs = qs.filter(Q(created__gte=start_date))
        if end_date:
            qs = qs.filter(Q(created__lte=end_date))
        return qs

    class Meta:
        model = Ticket
        fields = ["assigned_to", "queue", "status"]
