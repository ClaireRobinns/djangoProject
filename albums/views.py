from .forms import AlbumCreateForm
from django.shortcuts import render, redirect

def albums(request):
    context = {
        'forms': AlbumCreateForm,
    }
    return render(request, 'Black/albums.html', context=context)


def category(request, name):
    pass