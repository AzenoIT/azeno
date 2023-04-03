from django.urls import path

from .views import AccountTypeListAPIView, PlayerListAPIView

app_name = "players"

urlpatterns = [
    path("accounts/", AccountTypeListAPIView.as_view(), name="account_types"),
    path("players/", PlayerListAPIView.as_view(), name="players_list"),
]
