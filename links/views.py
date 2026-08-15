from django.shortcuts import redirect, render
from django.http import Http404
from django.contrib import messages
from .models import ShortLink, Click
from .forms import ShortLinkForm


def create_shortlink(request):
    if request.method == 'POST':
        form = ShortLinkForm(request.POST)
        if form.is_valid():
            shortlink = form.save(commit=False)

            if request.user.is_authenticated:
                shortlink.owner = request.user

            shortlink.save()

            messages.success(request, 'لینک کوتاه با موفقیت ساخته شد!')

            return render(request, 'links/success.html', {
                'shortlink': shortlink,
                'full_url': request.build_absolute_uri(f'/{shortlink.slug}/')
            })
    else:
        form = ShortLinkForm()

    return render(request, 'links/create.html', {'form': form})

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