import functools
from functools import wraps

from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from helpdesk import settings as helpdesk_settings


def available_attrs(*args, **kwargs):
    return functools.WRAPPER_ASSIGNMENTS


def protect_view(view_func):
    """
    Decorator for protecting the views checking user, redirecting
    to the log-in page if necessary or returning 404 status code
    """

    @wraps(view_func, assigned=available_attrs(view_func))
    def _wrapped_view(request, *args, **kwargs):
        if (
            not request.user.is_authenticated
            and helpdesk_settings.HELPDESK_REDIRECT_TO_LOGIN_BY_DEFAULT
        ):
            return HttpResponseRedirect(reverse("helpdesk:login"))
        elif (
            not request.user.is_authenticated
            and helpdesk_settings.HELPDESK_ANON_ACCESS_RAISES_404
        ):
            raise Http404
        return view_func(request, *args, **kwargs)

    return _wrapped_view
