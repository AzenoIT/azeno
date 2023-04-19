from django.urls import path

from . import views

app_name = "players"

urlpatterns = [
    path(
        "players/username/", views.NicknameGeneratorAPIView.as_view(), name="username"
    ),
    path("players/", views.PlayerCreateAPIView.as_view(), name="create-player"),
    path(
        "players/<uuid:uuid>/",
        views.PlayerRetrieveUpdateAPIView.as_view(),
        name="player_profile",
    ),
]
