from django.shortcuts import render, get_object_or_404
from .models import Album

def album_list(request):
    albums = Album.objects.all()
    return render(request, 'album_list.html', {'albums': albums})