from rest_framework import serializers

from .models import Game


class GameSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    platform = serializers.CharField(max_length=255)
    score = serializers.IntegerField()
    genre = serializers.CharField()
    editors_choice = serializers.BooleanField()
    game_id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        return Game.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.platform = validated_data.get('platform', instance.platform)
        instance.score = validated_data.get('score', instance.score)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.editors_choice = validated_data.get('editors_choice', instance.editors_choice)

        instance.save()
        return instance
