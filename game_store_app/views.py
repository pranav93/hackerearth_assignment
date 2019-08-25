from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import GameSerializer
from .models import Game


class GameListView(APIView):
    def get_queryset(self):
        queryset = Game.objects.all()

        title = self.request.query_params.get('title', None)
        platform = self.request.query_params.get('platform', None)
        genre = self.request.query_params.get('genre', None)

        if title is not None:
            queryset = queryset.filter(title=title)
        if platform is not None:
            queryset = queryset.filter(platform=platform)
        if genre is not None:
            queryset = queryset.filter(genre=genre)

        return queryset

    def get(self, request):
        games = self.get_queryset()
        serializer = GameSerializer(games, many=True)
        return Response({"games": serializer.data})

    def post(self, request):
        game = request.data.get('game')

        # Create an game from the above data
        serializer = GameSerializer(data=game)
        if serializer.is_valid(raise_exception=True):
            game_saved = serializer.save()
        return Response({"success": "Game '{}' created successfully".format(game_saved.title)})


class GameDetailView(APIView):
    def get(self, request, pk):
        game = self.get_object(pk)
        serializer = GameSerializer(game, many=False)
        return Response({"game": serializer.data})

    def put(self, request, pk):
        saved_game = get_object_or_404(Game.objects.all(), pk=pk)
        data = request.data.get('game')
        serializer = GameSerializer(instance=saved_game, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            game_saved = serializer.save()
        return Response({"success": "Game '{}' updated successfully".format(game_saved.title)})

    def delete(self, request, pk):
        game = self.get_object(pk)
        title = game.title
        game.delete()
        return Response({"success": "Game '{}' deleted successfully".format(title)})

    def get_object(self, pk):
        game = Game.objects.filter(pk=pk)
        if not game:
            raise Http404
        return game[0]
