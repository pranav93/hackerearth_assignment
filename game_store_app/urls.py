from django.urls import path

from .views import GameListView, GameDetailView


app_name = "game_store_app"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('games/', GameListView.as_view()),
    path('games/<int:pk>', GameDetailView.as_view())
]
