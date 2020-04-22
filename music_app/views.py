from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.urls import reverse
# Create your views here.


def home(requests):
    return HttpResponseRedirect(reverse('musician_list'))


def musician_list(request):
    context = {
        'musicians': Musician.objects.all()
    }
    return render(request, 'music_app/musician_list.html', context=context)


def musician_detail(request, id):
    context = {
        'musician': Musician.objects.get(id=id),
        'bands_albums': [(band, band.album_set.all()) for band in Musician.objects.get(id=id).band_set.all()]
    }
    return render(request, 'music_app/musician_detail.html', context=context)


def album_detail(request, id):
    context = {
        'album': Album.objects.get(id=id),
        'songs': Album.objects.get(id=id).song_set.all()
    }
    return render(request, 'music_app/album_detail.html', context=context)


def song_detail(request, id):
    context = {
        'song': Song.objects.get(id=id)
    }
    return render(request, 'music_app/song_detail.html', context=context)
