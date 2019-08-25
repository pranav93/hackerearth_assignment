from django.urls import path

from game_store_app.views.authentication import login, logout
from game_store_app.views.game_details import GameDetailView
from game_store_app.views.game_list import GameListView

app_name = "game_store_app"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('games/', GameListView.as_view()),
    path('games/<int:pk>', GameDetailView.as_view()),
    path('login/', login),
    path('logout/', logout)
]
