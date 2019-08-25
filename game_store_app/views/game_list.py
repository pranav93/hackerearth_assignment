from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from game_store_app.models import Game
from game_store_app.serializers import GameSerializer


class GameListView(APIView):
    permission_classes = (IsAuthenticated,)

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
