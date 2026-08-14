from django.shortcuts import redirect
from django.http import Http404
from .models import ShortLink, Click


def redirect_to_original(request, slug):
    try:
        shortlink = ShortLink.objects.get(slug=slug)

        Click.objects.create(
            link=shortlink,
            referrer=request.META.get('HTTP_REFERER', ''),
            user_agent=request.META.get('HTTP_USER_AGENT', '')
        )

        return redirect(shortlink.original_url)
    except ShortLink.DoesNotExist:
        raise Http404("لینک کوتاه پیدا نشد!")