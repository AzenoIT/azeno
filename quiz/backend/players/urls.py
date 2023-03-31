from django.urls import path
from . import views

app_name = "players"

urlpatterns = [
    path(
        "nickname-generator/", views.NicknameGeneratorAPIView.as_view(), name="nickname"
    ),
]
