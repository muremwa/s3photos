from django.views.generic import RedirectView
from django.conf import settings
from django.shortcuts import render


def photos_open(request, **kwargs):
    return render(request, 'open/index.html')


def photos_ng(request, **kwargs):
    return render(request, 'ng/index.html')


class NgAssets(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        if kwargs.get('path'):
            return f'{settings.STATIC_URL}ng/assets/{kwargs.get("path")}'

        return super().get_redirect_url(*args, **kwargs)
