from django.db import models

# Create your models here.


from django.db import models


class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)
    score = models.FloatField()
    genre = models.CharField(max_length=255)
    editors_choice = models.BooleanField()
