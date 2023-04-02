from django.urls import path

from . import views

app_name = "players"

urlpatterns = [
    path("players/", views.PlayerCreateAPIView.as_view(), name="create-player"),
]
