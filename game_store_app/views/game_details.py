import logging

from django.http import Http404
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from game_store_app.models import Game
from game_store_app.serializers import GameSerializer


logger = logging.getLogger(__name__)


class GameDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        game = self.get_object(pk)
        serializer = GameSerializer(game, many=False)
        return Response({"game": serializer.data})

    def put(self, request, pk):
        saved_game = get_object_or_404(Game.objects.all(), pk=pk)
        data = request.data.get('game')
        serializer = GameSerializer(instance=saved_game, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            logger.info('Updating game with id ' + str(pk))
            game_saved = serializer.save()
        return Response({"success": "Game '{}' updated successfully".format(game_saved.title)})

    def delete(self, request, pk):
        game = self.get_object(pk)
        title = game.title
        logger.info('Deleting game with id ' + str(pk))
        game.delete()
        return Response({"success": "Game '{}' deleted successfully".format(title)})

    def get_object(self, pk):
        game = Game.objects.filter(pk=pk)
        if not game:
            raise Http404
        return game[0]
