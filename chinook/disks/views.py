from django.shortcuts import render, get_object_or_404
from .models import Album
from django.db.models import Q

def album_list(request):
    query = request.GET.get('q')  # prende il testo inserito nel campo di ricerca
    if query:
        albums = Album.objects.filter( Q(title__icontains=query) | Q(artist__name__icontains=query))
    else:
        albums = Album.objects.all()
    return render(request, 'album_list.html', {
        'albums': albums,
        'query': query,
    })
    
def album_detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    tracks = album.track_set.all()
    return render(request, 'album_detail.html', {
        'album': album,
        'tracks': tracks
    })
    
