from django.shortcuts import render


def photos_open(request, **kwargs):
    return render(request, 'open/index.html')
