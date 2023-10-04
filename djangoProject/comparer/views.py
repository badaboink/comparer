from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Category, Playlist, Song
from .serializers import CategorySerializer, PlaylistSerializer, SongSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class PlaylistByCategoryView(viewsets.ModelViewSet):
    serializer_class = PlaylistSerializer

    def get_queryset(self):
        category = self.request.query_params.get('category')
        if category:
            return Playlist.objects.filter(category_id=category)
        else:
            return Playlist.objects.all()


class SongsInPlaylistView(viewsets.ModelViewSet):
    serializer_class = SongSerializer

    def get_queryset(self):
        playlist_id = self.request.query_params.get('playlist')
        if playlist_id:
            return Song.objects.filter(playlist__id=playlist_id)
        else:
            return Song.objects.all()
